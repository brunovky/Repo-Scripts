function verificarErros() {
        var msg = ''
        $('.required').each(function() {
            if ($(this).val() == '') {
                var labelText = $(this).prev().text()
                msg = msg + labelText.substr(0, labelText.length - 1) + ' é obrigatório. <p />'
            }
        })
        if (msg != '') {
            $('.view').removeClass('hide')
            $('#msg_error').html(msg)
            return true
        }
        return false
}

var app = angular.module('app', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{_');
    $interpolateProvider.endSymbol('_}');
})

function appController($scope, $http) {
    $scope.produtos = []

    $http.get('/rest/crud/listar_produtos').success(function(lista) {
        $scope.produtos = lista
    })

    $scope.salvarProduto = function() {
        if (!verificarErros()) {
            var produto = {
                'nome': $scope.nome,
                'descricao': $scope.descricao,
                'preco': $scope.preco,
                'imagem': $scope.imagem
            }
            $http.post('/rest/crud/salvar_produto', produto).success(function(obj) {
                alert('Produto cadastrado com sucesso')
                $scope.nome = ''
                $scope.descricao = ''
                $scope.preco = ''
                $scope.imagem = ''
            })
        }
    }

    $scope.editarProduto = function(produto) {
        produto.editando = true;
    }

    $scope.confirmarEdicao = function(produto){
        produto.editando = false;
        params = {"id": produto.id,
                  "nome": produto.nome,
                  "imagem": produto.imagem,
                  "preco": produto.preco
        }
        $http.post('/rest/crud/editar_produto', params);
    }

    $scope.removerElemento = function(produto, index){
        $scope.produtos.splice(index, 1);
        produto.editando = false;
        $http.post('/rest/crud/remover_produto', {"id": produto.id});
    }

    $scope.abrirModalProduto = function() {
        $('#modal-container' + $scope.index).modal()
    }
}