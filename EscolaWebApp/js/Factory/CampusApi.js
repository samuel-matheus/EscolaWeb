// campus factory
var campusFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase+ "/campi")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/campi/" + encodeURI(id))
  };
  var _cadastrar = function(campus) {
    return $http.post(urlBase + "/campus", campus)
  };
  var _atualizar = function(campus) {
    return $http.put(urlBase + "/campus/" + encodeURI(id), campus)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("campusApi", campusFactory);
