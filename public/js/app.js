angular.module('routerApp', ['routerRoutes'])

.controller('mainController', function() {
	var vm = this;
})

.controller('homeController', function() {
	var vm = this;

	vm.titles = [
		{ name: 'Select a mode', function: 'Next' },
		{ name: 'Pick a candidate', function: 'View results' },
		{ name: 'Results', function: 'Try again' }
	];
})

.controller('aboutController', function() {
	var vm = this;

	vm.members = [
		{ name: 'William Wu', role: 'Full Stack Developer', 
			bio: 'Interested in mobile development and experienced in full stack\
				  development and data science technology.',
			contact: 'will.go.code@gmail.com',
			pic: '/assets/images/will.jpg' },
		{ name: 'Ada Chen', role: 'Front End Developer', 
			bio: 'Recently came back from Miami. Continues to watch videos\
				  on AngularJS. Currently dating Jimmy.',
			contact: 'ada77.chen@gmail.com',
			pic: '/assets/images/ada.jpg' },
		{ name: 'Fabio Francois', role: 'Back End Developer', 
			bio: 'vim > emacs',
			contact: 'ffrancois749@gmail.com',
			pic: '/assets/images/david.jpg' },	
		{ name: 'Brandon Troche', role: 'Backend Developer', 
			bio: 'Brandon is working on half of the backend. In addition to backend,\
				  he also works well in iOS full stack development and Object \
				  Oriented Development as a whole.',
			contact: 'bttroche@gmail.com',
			pic: '/assets/images/brandon.jpg' }
	];
});
