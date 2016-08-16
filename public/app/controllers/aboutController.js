angular.module('aboutController', [])

.controller('aboutController', function($scope) {
    $scope.pageClass = 'page-about';
    $scope.members = [
        { name: 'William Wu', role: 'Full Stack Developer',
            bio: 'Interested in mobile development, experienced in full stack\
                  development and familiar with data science technology and\
				  algorithms. Also versatile, and quick to pickup on new technologies.',
            contact: 'will.go.code@gmail.com',
            pic: '/assets/images/will.jpg' },
        { name: 'Ada Chen', role: 'Front End Developer',
            bio: 'New to web development and assisting with Front-End tasks. Interested\
				  in application testing and analysis.',
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
