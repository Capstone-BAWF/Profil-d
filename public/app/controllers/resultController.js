angular.module('resultController', [])

.controller('resultController', function($scope, $http, $rootScope, $location, $timeout) {
        $scope.pageClass = 'page-result';
        $scope.processing = true;
		$scope.imgSrc = "/assets/images/";
		
        $timeout(callAtTimeout, 5000);

        function callAtTimeout(){
            $http.get('/api/resultGet')
                .success(function(data) {
                    $scope.processing = false;
                    $scope.result = data;
					$scope.imgSrc = "/assets/images/" + $scope.result[0].candidate + ".jpg";
                	$scope.candidateName = $scope.result[0].candidate;
					if($scope.candidateName == 'donny')
						$scope.candidateName = 'Donald Trump';
					else if($scope.candidateName == 'hillary')
						$scope.candidateName = 'Hillary Clinton';
					else
						$scope.candidateName = 'Bernie Sanders';
				})  
                .error(function(data) {
                    console.log('Error: ' + data);
            });   
        };        
	
		$scope.submit = function() {
			$location.path('/');
		};
});
