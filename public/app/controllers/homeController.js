angular.module('homeController', ['pythonService'])

.controller('homeController', function($scope, $http, $rootScope, $location, $routeParams) {
        $scope.pageClass = 'page-home';
        $scope.twitterName = "";
		
        $scope.submit = function(isValid) {
            $http.post("/api/userGen/" + $scope.twitterName)
            .success(function(twitterName, err) {
            	$location.path('/candidate');
			})
        };
});
