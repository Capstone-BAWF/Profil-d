angular.module('pythonService', [])

.factory('Python', function($http) {
		var pythonFactory = {};

		pythonFactory.getResults = function() {
			return $http.get('/api/resultGet');
		};

		pythonFactory.setCandidateAndExec = function(candidate) {
			return $http.post('/api/candidatePick/' + candidate);
		};

		pythonFactory.setUser = function(user) {
			return $http.post('/api/userGen' + user);
		};

		return pythonFactory;
});

