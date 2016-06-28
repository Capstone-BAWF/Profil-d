var express = require('express'), app = express();
var mongoose = require('mongoose');
var bodyParser= require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var port = process.env.PORT || 8080;
// var path = require('path');

// Define root directory
app.get('/', function(req, res){
		res.sendFile(path.join(__dirname + '/index.html'));
});

// Creating admin routes
var adminRouter = express.Router();

// Middleware to log something before page loads
adminRouter.use(function(req, res, next){
		console.log(req.method, req.url);
		next();
});

// Root of admin page
adminRouter.get('/', function(req, res){
		res.send('I am the dashboard!');
});

// /admin/users/ page, will wait for parameter :name
adminRouter.get('/users/:name', function(req, res){
		res.send('hello ' + req.params.name+ '!');
});

// /admin/users/ page
adminRouter.get('/users', function(req, res){
		res.send('I show all the users!');
});

// Function to determine what to do for the :name parameter
adminRouter.param('name', function(req, res, next, name){
		console.log('doing name validations on ' + name);
		req.name = name;
		next();
});

// /admin/posts/ page
adminRouter.get('/posts', function(req, res){
		res.send('I show all the posts!');
});

// app will use adminRouter for all pages with /admin/ 
app.use('/admin', adminRouter);

// Listen on this port
app.listen(1337);
console.log('1337 is the magic port!');
