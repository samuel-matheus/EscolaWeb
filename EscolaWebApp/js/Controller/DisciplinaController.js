var disciplinaController = function($scope, $mdToast, disciplinaApi){
  $scope.disciplina={};

  $scope.cadastrar = function() {
    disciplinaApi.cadastrar($scope.disciplina)
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
    $scope.formdisciplina.$setPristine();
  }
}
app.controller('DisciplinaController', disciplinaController);
