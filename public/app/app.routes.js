// inject ngRoute for all our routing needs
angular.module('routerRoutes', ['ngRoute'])

// configure our routes
.config(function($routeProvider, $locationProvider) {
    $routeProvider

        // route for the home page
        .when('/', {
				templateUrl : 'app/views/pages/home.html',
				controller  : 'homeController'
        })

        // route for the about page
        .when('/about', {
				templateUrl : 'app/views/pages/about.html',
				controller  : 'aboutController'
        })

		.when('/candidate', {
				templateUrl : 'app/views/pages/candidate.html',
				controller  : 'candidateController'
		})

		.when('/result', {
				templateUrl : 'app/views/pages/result.html',
				controller  : 'resultController'
		});
    
	$locationProvider.html5Mode(true);
});
