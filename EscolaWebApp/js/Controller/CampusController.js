var campusController = function($scope, $mdToast, campusApi){
  $scope.campus={};

  $scope.cadastrar = function() {
    campusApi.cadastrar($scope.campus)
      .then(function(response) {})
      .catch(function(error) {
        var toast = $mdToast.simple()
        .textContent('Algum problema ocorreu no envio dos dados.')
        .position('bottom center')
        .action('OK')
        .hideDelay(6000)
        .toastClass('my-success');
        $mdToast.show(toast);
      });
    $scope.formcampus.$setPristine();
  }
}
app.controller('CampusController', campusController);
