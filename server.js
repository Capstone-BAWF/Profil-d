// get the things we need
var express = require('express');
var app     = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var config = require('./config');
var path = require('path');

// body parser gets information from POST requests
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// configure app to handle CORS requests
app.use(function(req, res, next) {
		res.setHeader('Access-Control-Allow-Origin', '*');
		res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
		res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type, Authorization');
		next();
});

// log all requests to the console
app.use(morgan('dev'));

// connect to database
mongoose.connect(config.database);

// set the public folder to serve public assets
app.use(express.static(__dirname + '/public'));

var apiRoutes = require('./app/routes/api')(app, express);
app.use('/api', apiRoutes);

// set up our one route to the index.html file
app.get('*', function(req, res) {
	res.sendFile(path.join(__dirname + '/public/app/views/index.html'));
});

// start the server on port 8080 (http://localhost:8080)
app.listen(config.port);
console.log('Magic happens on port ' + config.port);
