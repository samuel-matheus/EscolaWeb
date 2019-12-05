app.config(function ($routeProvider, $locationProvider) {

    // Remover a exclamação (!) da URL
    var SEM_PREFIXO = '';
    $locationProvider.hashPrefix(SEM_PREFIXO);

    // Utilizando o HTML5 History API
    //$locationProvider.html5Mode(true);

    // Atualizar os módulos passados no app.js adicionando o 'ui.router'.
    // Mover todas as rotas já definidas no router.js para o arquivo state.js.
    // Verificar o modelo utilizado para o $stateProvider presente no state.js que é diferente.
    // Não esquecer de importar no index o script state.js .
    // Mudar no index.html o atributo ng-view para o ui-view.
    $routeProvider
      .when('/', {
        templateUrl : 'Home.html',
        controller  : 'HomeController'
      })
      .when('/aluno', {
        templateUrl : 'Aluno.html',
        controller  : 'AlunoController'
      })
      .when('/campus', {
        templateUrl : 'Campus.html',
        controller  : 'CampusController'
      })
      .when('/curso', {
        templateUrl : 'Curso.html',
        controller  : 'CursoController'
      })
      .when('/disciplina', {
        templateUrl : 'Disciplina.html',
        controller  : 'DisciplinaController'
      })
      .when('/endereco', {
        templateUrl : 'Endereco.html',
        controller  : 'EnderecoController'
      })
      .when('/escola', {
        templateUrl : 'Escola.html',
        controller  : 'EscolaController'
      })
      .when('/professor', {
        templateUrl : 'Professor.html',
        controller  : 'ProfessorController'
      })
      .when('/turma', {
        templateUrl : 'Turma.html',
        controller  : 'TurmaController'
      })
      .when('/turno', {
        templateUrl : 'Turno.html',
        controller  : 'TurnoController'
      })
    .otherwise({redirectTo: '/'});
});
