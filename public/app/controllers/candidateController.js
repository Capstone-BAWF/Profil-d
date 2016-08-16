angular.module('candidateController', [])

.controller('candidateController', function($scope, $http, $rootScope, $location) {
        $scope.pageClass = 'page-candidate';
        $scope.candidate = "";

        $scope.submit = function() {
            $http.post("/api/candidatePick/" + $scope.candidate)
                .success(function(candidate, err) {
                	$location.path('/result');
				})
        };  
        
});
