// Factory Disciplina
var disciplinaFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/disciplinas")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/disciplinas/" + encodeURI(id))
  };
  var _cadastrar = function(disciplina) {
    return $http.post(urlBase + "/disciplina", disciplina)
  };
  var _atualizar = function(disciplina) {
    return $http.put(urlBase + "/disciplina/" + encodeURI(id), disciplina)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("disciplinaApi", disciplinaFactory);
