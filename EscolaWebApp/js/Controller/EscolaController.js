var escolaController = function($scope, $mdToast, escolaApi){
  $scope.escola={};


  $scope.cadastrar = function() {
    escolaApi.cadastrar($scope.escola)
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
    $scope.formescola.$setPristine();
  }
}
app.controller('EscolaController', escolaController);
