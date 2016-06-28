// Load up modules, create schema
var mongoose=require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

// Define user schema
var UserSchema = new Schema({
		name: String,
	username: { type: String, required: true, index: { unique: true}},
	password: { type: String, required: true, select: false}
});

// Before saving, hash the password and set password to hashed password
UserSchema.pre('save', function(next){
		var user= this;
		if(!user.isModified('password')) return next();

		bcrypt.hash(user.password, null, null, function(err, hash){
			if(err) return next(err);

			user.password = hash;
			next();
		});
});

// Compare password 
UserSchema.methods.comparePassword = function(password){
	var user = this;
	return bcrypt.compareSync(password, user.password);
};

// Save the new user
module.exports = mongoose.model('User', UserSchema);
