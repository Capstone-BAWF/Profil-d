var mongoose = require('mongoose');
var Schema       = mongoose.Schema;
var bcrypt       = require('bcrypt-nodejs');

var TweetSchema   = new Schema({
    name: String,
});

module.exports = mongoose.model('Tweet', TweetSchema);

