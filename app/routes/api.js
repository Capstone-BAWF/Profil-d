var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
var User       = require('../models/user');
var jwt        = require('jsonwebtoken');
var config     = require('../../config');
var TwitterName = require('../models/twitterName');
var superSecret = config.secret;

module.exports = function(app, express) {
	
	var apiRouter = express.Router();
	var user = "";
	
	apiRouter.use(function(req, res, next) {
			console.log('Somebody is here.');
			next();
	});

	apiRouter.get('/', function(req, res) {
			var options = { mode: 'text',
					scriptPath: './python',
					args: ['dicks']
			};
	/*
			var pyshell = new PythonShell('jew.py', options);
			
			pyshell.on('message', function (message) {
				var tip = message;
				console.log(tip);
			});

			PythonShell.run('jew.py', options, function (err) {
				if (err) throw err;
			});

			res.json({ message: "I'm a jew!" });
	*/
	});

	apiRouter.use(function(req, res, next) {
			console.log('Main page middleware.');
			next();
	});
	
	apiRouter.post('/userGen/:twitterName', function(req, res, next) {
			user = "";
			user = req.params.twitterName;
			
			res.json({ message: "Hello " + user});
	});

	apiRouter.get('/candidatePick/:candidate', function(req, res, next) {
			var candidate = req.params.candidate;

			var options = { mode: 'text',
							scriptPath: './python',
							args: [user, candidate]
			};

			PythonShell.run('jew.py', options, function(err) {
				if (err) throw err;
			});

			console.log(candidate);
			console.log(user);
			res.json({ message: "Hello" + candidate });
	});

	apiRouter.get('/resultGet/', function(req, res, next) {
			console.log("Will retrieve result from MongoDB for the User.");
	});

	return apiRouter;
};
