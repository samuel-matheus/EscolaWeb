var professorController = function($scope, $mdToast, professorApi){
  $scope.professor={};

  $scope.cadastrar = function() {
    professorApi.cadastrar($scope.professor)
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
    $scope.formprofessor.$setPristine();
  }
}
app.controller('ProfessorController', professorController);
