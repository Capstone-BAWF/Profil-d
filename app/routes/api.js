var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
var User       = require('../models/user');
var jwt        = require('jsonwebtoken');
var config     = require('../../config');
var TwitterName = require('../models/twitterName');
var superSecret = config.secret;

module.exports = function(app, express) {
	
	var apiRouter = express.Router();

	apiRouter.use(function(req, res, next) {
			console.log('Somebody is a jew right now!');
			next();
	});

	apiRouter.get('/', function(req, res) {
			var options = { mode: 'text',
					scriptPath: './python',
					args: ['dicks']
			};

			var pyshell = new PythonShell('jew.py', options);
			
			pyshell.on('message', function (message) {
				var tip = message;
				console.log(tip);
			});

			PythonShell.run('jew.py', options, function (err) {
				if (err) throw err;
			});

			res.json({ message: "I'm a jew!" });
	});

	apiRouter.use(function(req, res, next) {
			next();
	});
	
	apiRouter.post('/userGen/:twitterName', function(req, res, next) {
			var user = req.params.twitterName;
			
			var options = { mode: 'text',
							scriptPath: './python', 
							args: [user]
			};

			PythonShell.run('jew.py', options, function(err) {
				if (err) throw err;
			});

			res.json({ message: "Hello " + user});
	});

	return apiRouter;
};
