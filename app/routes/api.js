var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
var User       = require('../models/user');
var jwt        = require('jsonwebtoken');
var config     = require('../../config');
var TwitterName = require('../models/twitterName');
var Results 	= require('../models/results');
var superSecret = config.secret;

module.exports = function(app, express) {
	
	var apiRouter = express.Router();
	var user = "";
	var candidate = "";

	apiRouter.use(function(req, res, next) {
			console.log('Somebody is here.');
			next();
	});

	apiRouter.get('/', function(req, res) {
			res.json({ message: "On home page." });
	});

	apiRouter.use(function(req, res, next) {
			console.log('Main page middleware.');
			next();
	});
	
	apiRouter.post('/userGen/:twitterName', function(req, res, next) {
			user = req.params.twitterName;
			console.log("Twitter is: " + user);
			res.json({ message: "Hello " + user});
	});

	apiRouter.get('/candidatePick/:candidate', function(req, res, next) {
			candidate = req.params.candidate;
			
			var options = { mode: 'text',
							scriptPath: './Tweet_Analysis',
							args: [user, candidate]
			};
			
			PythonShell.run('Candidates.py', options, function(err) {
				if (err) throw err;
			});
			
			console.log("Candidate is: " + candidate);
			res.json({ message: "Hello" + candidate });
	});

	apiRouter.get('/resultGet/', function(req, res) {
			var search = "c^" + user + "/" + candidate;
			console.log("Search term is: " + search);
			Results.find(search, function(err, result) {
				if (err) res.send(err);
				console.log(result);
				res.json(result);
			});
			user = "";
			candidate = "";
	});

	return apiRouter;
};
