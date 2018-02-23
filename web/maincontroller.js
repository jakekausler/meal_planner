angular.module('meals', ['ngMaterial', 'ngSanitize', 'materialCalendar', 'md.data.table'])
    .config(function($mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('indigo')
            .accentPalette('pink')
            .warnPalette('red')
            .backgroundPalette('indigo')
    })
    .controller('mainController', function($scope, $http, $mdToast, $mdMedia, $mdDialog, $filter) {
        $scope.calendar = [];
        $scope.selectedDate = null;
        $scope.firstDayOfWeek = 0;
        $scope.setDirection = function(direction) {
            $scope.direction = direction;
        };
        $scope.dayClick = function(date) {};
        $scope.prevMonth = function(data) {
            $scope.GetCalendar(data);
        };
        $scope.nextMonth = function(data) {
            $scope.GetCalendar(data);
        };
        $scope.setDayContent = function(date) {
            return "<p></p>";
        };
        $scope.GetCalendar = function(data = null) {
            date = new Date();
            startDate = new Date(date.getFullYear(), date.getMonth(), 1);
            endDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
            if (data) {
                startDate = new Date(data.year, data.month - 1, 1);
                endDate = new Date(data.year, data.month, 0);
            }
            $http({
                url: "calendar",
                method: "GET",
                params: {
                    startdate: startDate,
                    enddate: endDate
                }
            }).then(function(res) {
                $scope.calendar = res.data;
            }, function(res) {
                $mdToast.showSimple("Failed: " + res);
            });
        }
        $scope.GetCalendar();
    });
