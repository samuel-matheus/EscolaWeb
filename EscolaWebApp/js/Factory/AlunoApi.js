var alunoFactory = function($http) {
  var urlBase = "localhost:5000";

  var _listar = function() {
    return $http.get(_urlBase + "/alunos")
  };
  var _buscarPorId = function(id) {
    return $http.get(_urlBase + "/alunos/" + encodeURI(id))
  };
  var _cadastrar = function(aluno) {
    return $http.post(urlBase + "/aluno", aluno)
  };
  var _atualizar = function(aluno) {
    return $http.put(urlBase + "/aluno/" + encodeURI(id), aluno)
  };

  return {
    listar: _listar,
    buscarPorId: _buscarPorId,
    cadastrar: _cadastrar,
    atualizar: _atualizar
  };
}
app.factory("alunoApi", alunoFactory);
