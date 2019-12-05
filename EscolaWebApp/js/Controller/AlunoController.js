var alunoController = function($scope, $mdToast, alunoApi){
  $scope.aluno={};

  $scope.cadastrar = function() {
    alunoApi.cadastrar()
    //se der certo vai pro THEN, se nao, CATCH
      .then(function(response) {
          console.log("Requisicao enviada e recebida com sucesso");
          console.log(response);
      })

      .catch(function(error) {
        var toast = $mdToast.simple()
        .textContent('Algum problema ocorreu no envio dos dados.')
        .position('bottom center')
        .action('OK')
        .hideDelay(6000)
        .toastClass('my-success');
        $mdToast.show(toast);
      });
    /*
    alunoApi.cadastrar($scope.aluno)
      .then(function(response) {})
      .catch(function(error) {});
    $scope.formaluno.$setPristine();
    */
  }
}
app.controller('AlunoController', alunoController);
