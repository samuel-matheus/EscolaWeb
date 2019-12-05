var enderecoController = function($scope, $mdToast, enderecoApi){
  $scope.endereco={};

  $scope.cadastrar = function() {
    enderecoApi.cadastrar($scope.endereco)
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
    $scope.formendereco.$setPristine();
  }
}
app.controller('EnderecoController', enderecoController);
