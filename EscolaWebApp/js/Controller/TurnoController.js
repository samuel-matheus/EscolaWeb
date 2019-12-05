var turnoController = function($scope, $mdToast, turnoApi){
  $scope.turno={};

  $scope.cadastrar = function() {
    turnoApi.cadastrar($scope.turno)
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
    $scope.formturno.$setPristine();
  }
}
app.controller('TurnoController', turnoController);
