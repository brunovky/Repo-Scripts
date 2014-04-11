# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Produto

def vitrine(_write_tmpl, pesquisa):
    produto = Produto(nome='Produto 1', descricao='', preco=199.99, imagem='produto-1')
    produto.put()
    produto2 = Produto(nome='Produto 2', descricao='', preco=29.99, imagem='produto-2')
    produto2.put()
    produto3 = Produto(nome='Produto 3', descricao='', preco=59.99, imagem='produto-3')
    produto3.put()
    produtos = Produto.query(Produto.nome >= pesquisa).order(Produto.nome).fetch()
    dict = {'produtos': produtos}
    _write_tmpl('/templates/shop.html', dict)

def descricao(_write_tmpl, produto):
    produtoProcurado = Produto.query().fetch()
    dict = {'produto': produtoProcurado}
    _write_tmpl('/templates/description.html', dict)