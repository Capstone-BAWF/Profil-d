var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
var User       = require('../models/user');
var jwt        = require('jsonwebtoken');
var config     = require('../../config');

var superSecret = config.secret;

module.exports = function(app, express) {

	var apiRouter = express.Router();

	apiRouter.get('/', function(req, res) {
			PythonShell.run('jew.py', function (err) {
				if (err) throw err;
			});
			res.json({ message: "I'm a jew!" });
	});

	return apiRouter;
};
