angular.module('PythonCaller', []).factory('TwitterName', ['$http, function($http) {
		return {
			create : function(twitterName) {
				return $http.post('/api/userGen', twitterName);
			}
		}
}]);
