angular.module('homeController', [])

.controller('homeController', function(User) {
	var vm = this;

	vm.titles = [
        { name: 'Select a mode', function: 'Next' },
        { name: 'Pick a candidate', function: 'View results' },
        { name: 'Results', function: 'Try again' }
    ];
});

