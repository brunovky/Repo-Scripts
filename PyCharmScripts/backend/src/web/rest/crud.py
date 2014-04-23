# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Produto

def vitrine(_write_tmpl, pesquisa):
    produtos = Produto.query(Produto.nome >= pesquisa).order(Produto.nome).fetch()
    dict = {'produtos': produtos}
    _write_tmpl('/templates/shop.html', dict)

def descricao(_write_tmpl, produto):
    produtoProcurado = Produto.query().fetch()
    dict = {'produto': produtoProcurado}
    _write_tmpl('/templates/description.html', dict)

def cadastrar_produto(_write_tmpl):
    _write_tmpl('/templates/add_product.html')

def salvar_produto(_handler, nome, descricao, preco, imagem):
    preco = float(preco)
    produto = Produto(nome=nome, descricao=descricao, preco=preco, imagem=imagem)
    produto.put()