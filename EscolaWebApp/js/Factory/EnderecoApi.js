
// Factory endereco
var enderecoFactory = function($http) {

  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/enderecos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/enderecos/" + encodeURI(id))
  };
  var _cadastrar = function(endereco) {
    return $http.post(urlBase + "/endereco", endereco)
  };
  var _atualizar = function(curso) {
    return $http.put(urlBase + "/endereco/" + encodeURI(id), endereco)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}

app.factory("enderecoApi", enderecoFactory);
