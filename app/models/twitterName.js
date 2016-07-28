var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;
var bcrypt       = require('bcrypt-nodejs');

// user schema 
var TwitterNameSchema   = new Schema({
    username: String,
});

module.exports = mongoose.model('TwitterName', TwitterNameSchema);

