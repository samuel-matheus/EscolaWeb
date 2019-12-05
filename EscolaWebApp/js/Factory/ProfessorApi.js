// Factory Professor
var professorFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/professores")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/professores/" + encodeURI(id))
  };
  var _cadastrar = function(professor) {
    return $http.post(urlBase + "/professor", professor)
  };
  var _atualizar = function(professor) {
    return $http.put(urlBase + "/professor/" + encodeURI(id), professor)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("professorApi", professorFactory);
