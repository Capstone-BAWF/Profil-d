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
				  development.',
			contact: 'will.go.code@gmail.com',
			pic: '/assets/images/will.jpg' },
		{ name: 'Ada Chen', role: 'Front End Developer', 
			bio: 'Recently came back from Miami. Continues to watch videos\
				  on AngularJS.',
			contact: 'ada77.chen@gmail.com',
			pic: '/assets/images/ada.jpg' },
		{ name: 'Fabio Francois', role: 'Back End Developer', 
			bio: 'A candidate at Google, Fabio Francois plays a lot of games\
				  when he is rarely working.',
			contact: 'fabio.francois@gmail.com',
			pic: '/assets/images/david.jpg' },	
		{ name: 'Brandon Troche', role: 'Backend Developer', 
			bio: 'Main focus is game development. Has a game on Apple\'s App Store\
				  called Tap N Slash',
			contact: 'bttroche@gmail.com',
			pic: '/assets/images/brandon.jpg' }
	];
});
