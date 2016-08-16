var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
var async 		= require('async');
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

	apiRouter.get('/', function(req, res) {
			user = "";
			candidate = "";
			res.json({ message: "On home page." });
	});
	
	apiRouter.post('/userGen/:twitterName', function(req, res) {
			user = req.params.twitterName;
			console.log("Twitter is: " + user);
			res.json({ message: "Hello " + user});
	});

	apiRouter.post('/candidatePick/:candidate', function(req, res) {
			candidate = req.params.candidate;
			var processing = true;

			var options = { mode: 'text',
							scriptPath: './Tweet_Analysis',
							args: [user, candidate]
			};

			console.log("Candidate is: " + candidate);
			console.log("Running Python Script.");
			var pyshell = new PythonShell('Candidates.py', options);
			pyshell.on('message', function (message) {
				res.json({ message: Error });
			});
			console.log("Python Script Finished.");
			res.json({ message: "Hello" + candidate });
	});

	apiRouter.get('/resultGet/', function(req, res, next) {
			var search = "c^" + user + "/" + candidate;
			console.log("Search term is: " + search);
			Results.find({'key': search}).limit(1).sort({dateAdded: 'descending'})
			.exec(function(err, result) {
				if (err) res.send(err);

				console.log(result);
				res.json(result);
			});
	});

	return apiRouter;
};
