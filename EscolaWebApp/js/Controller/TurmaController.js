var turmaController = function($scope, $mdToast, turmaApi){
  $scope.turma={};

  $scope.cadastrar = function() {
    turmaApi.cadastrar($scope.turma)
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
    $scope.formturma.$setPristine();
  }
}
app.controller('TurmaController', turmaController);
