// Factory Turma
var turmaFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/turmas")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/turmas/" + encodeURI(id))
  };
  var _cadastrar = function(turma) {
    return $http.post(urlBase + "/turma", turma)
  };
  var _atualizar = function(turma) {
    return $http.put(urlBase + "/turma/" + encodeURI(id), turma)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("turmaApi", turmaFactory);
