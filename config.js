module.exports = {
	'port': process.env.PORT || 8080,

	//for production
	//'database': 'mongodb://william:lemons@ds023475.mlab.com:23475/profild',
	
	//for local
	'database': 'mongodb://localhost:27017/tweetLibrary',
	'secret': 'capstoneisthebest'
};
