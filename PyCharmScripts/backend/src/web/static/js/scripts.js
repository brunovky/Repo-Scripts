var app = angular.module('app', [])
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{_');
    $interpolateProvider.endSymbol('_}');
})

function appController($scope, $http) {
    $scope.produtos = []

    $http.get('/rest/crud/listar_produtos').success(function(lista) {
        $scope.produtos = lista
    })

    $scope.verificarErros = function () {
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

    $scope.abrirModalProduto = function() {
        $('#modal-container' + $scope.index).modal()
    }
}