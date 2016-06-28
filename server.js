// Load modules
var express = require('express'), app = express();
var mongoose = require('mongoose');
var bodyParser= require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var port = process.env.PORT || 8080;
var path = require('path');
var User = require('./app/models/user');

// Body parser module will allow us to grab information from POST requests
app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());

// Configure app to handle CORS requests
app.use(function(req, res, next) {
		res.setHeader('Access-Control-Allow-Origin', '*');
		res.setHeader('Access-Control-Allow-Methods', 'Get, POST');
		res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type, \
			Authorization');
		next();
});

// Log requests to console
app.use(morgan('dev'));

// Routes for API

// Root page
app.get('/', function(req, res){
		res.sendFile(path.join(__dirname +'/index.html'));
});

// Router for /api/ 
var apiRouter = express.Router();

// Middleware for /api/
apiRouter.use(function(req, res, next){
		console.log('Somebody just came to our app!');
		//Next will go to the next route so it doesn't stop here.
		next();
});

// /api/ root 
apiRouter.get('/', function(req, res) {
		res.json({ message: 'Welcome to the API!' });
});

// Register routes
app.use('/api', apiRouter);

app.listen(port);

console.log('Magic happens on port ' + port);

mongoose.connect('mongodb://localhost:27017/newDb');
