from mock.mock import Mock
from base import GAETestCase
from web.rest import crud
from web.rest.rest import Produto
import json

class RestTests(GAETestCase):
    def test_vitrine(self):
        resposta_mock = Mock()
        crud.vitrine(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/shop.html')

    def test_listar_produtos(self):
        produto = Produto(id=1, nome='Teste', imagem='Teste', preco=1.99)
        produto.put()
        produtos = Produto.query().fetch()
        dict = [{'id': p.id, 'nome': p.nome, 'imagem': p.imagem, 'preco': p.preco} for p in produtos]
        resposta_mock = Mock()
        crud.listar_produtos(resposta_mock)
        json_str = json.dumps(dict)
        resposta_mock.write.assert_called_once_with(json_str)

    def test_cadastrar_produto(self):
        resposta_mock = Mock()
        crud.cadastrar_produto(resposta_mock)
        resposta_mock.assert_called_once_with('/templates/add_product.html')

    def test_salvar_produto(self):
        produto = Produto(nome='Teste', imagem='Teste', preco=1.99, descricao='Teste')
        resposta_mock = Mock()
        crud.salvar_produto(resposta_mock, produto.nome, produto.descricao, produto.preco, produto.imagem)
        produto = Produto.query(Produto.id == 1).get()
        assert produto.nome == 'Teste'

    def test_editar_produto(self):
        produto = Produto(nome='Teste', imagem='Teste', preco=1.99, descricao='Teste')
        produto.max_id()
        produto.put()
        crud.editar_produto(produto.id, produto.nome, produto.imagem, 2.99)
        produto = Produto.query(Produto.id == 1).get()
        assert produto.preco == 2.99

    def test_remover_produto(self):
        produto = Produto(nome='Teste', imagem='Teste', preco=1.99, descricao='Teste')
        produto.max_id()
        produto.put()
        crud.remover_produto(produto.id)
        produto = Produto.query(Produto.id == 1).get()
        assert not produto
