var cursoController = function($scope, $mdToast, cursoApi){
  $scope.curso={};

  $scope.cadastrar = function() {
    cursoApi.cadastrar($scope.curso)
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
    $scope.formcurso.$setPristine();
  }
}
app.controller('CursoController', cursoController);
