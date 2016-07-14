// inject ngRoute for all our routing needs
angular.module('routerRoutes', ['ngRoute'])

// configure our routes
.config(function($routeProvider, $locationProvider) {
    $routeProvider

        // route for the home page
        .when('/', {
				templateUrl : 'app/views/pages/home.html',
				controller  : 'homeController',
				controllerAs: 'home'
        })

        // route for the about page
        .when('/about', {
				templateUrl : 'app/views/pages/about.html',
				controller  : 'aboutController',
				controllerAs: 'about'
        })

		.when('/login', {
				templateUrl : 'app/views/pages/login.html',
				controller  : 'loginController',
				controllerAs: 'login'
		})
    
	$locationProvider.html5Mode(true);
});
