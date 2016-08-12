var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

var ResultSchema = new Schema({
		key: String,
		percentage: { type: Number, multipleOf: 1.0 },
		candidate: String,
		user: String
});

module.exports = mongoose.model('Result', ResultSchema);
