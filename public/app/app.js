var profild = angular.module('profild', ['ngAnimate', 'routerRoutes'])

// CONTROLLERS
profild.controller('mainController', function($scope) {
		$scope.pageClass = 'page-main';
});

profild.controller('homeController', function($scope) {
		$scope.pageClass = 'page-home';
		$scope.twitterName = "";
});

profild.controller('candidateController', function($scope) {
		$scope.pageClass = 'page-candidate';
		$scope.candidate = "";
});

profild.controller('resultController', function($scope) {
		$scope.pageClass = 'page-result';
		$scope.result = "";	
});

profild.controller('aboutController', function($scope) {
	$scope.pageClass = 'page-about';
	$scope.members = [
        { name: 'William Wu', role: 'Full Stack Developer',
            bio: 'Interested in mobile development and experienced in full stack\
                  development and data science technology.',
            contact: 'will.go.code@gmail.com',
            pic: '/assets/images/will.jpg' },
        { name: 'Ada Chen', role: 'Front End Developer',
            bio: 'New to web development but interested. Loves to play games.',
            contact: 'ada77.chen@gmail.com',
            pic: '/assets/images/boo.jpg' },
        { name: 'Fabio Francois', role: 'Back End Developer',
            bio: 'working on backend or whatever',
            contact: 'ffrancois749@gmail.com',
            pic: '/assets/images/fabs.jpg' },
        { name: 'Brandon Troche', role: 'Backend Developer',
            bio: 'Brandon is working on half of the backend. In addition to backend,\
                  he also works well in iOS full stack development and Object \
                  Oriented Development as a whole.',
            contact: 'bttroche@gmail.com',
            pic: '/assets/images/brandon.jpg' }
    ];
});

// 
