# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Produto
import json

def vitrine(_write_tmpl):
    _write_tmpl('/templates/shop.html')

def listar_produtos(_resp):
    produtos = Produto.query().order(Produto.nome).fetch()
    dict = [{'id': p.id, 'nome': p.nome, 'imagem': p.imagem, 'preco': p.preco} for p in produtos]
    _resp.write(json.dumps(dict))

def descricao(_write_tmpl, produto):
    produtoProcurado = Produto.query().fetch()
    dict = {'produto': produtoProcurado}
    _write_tmpl('/templates/description.html', dict)

def cadastrar_produto(_write_tmpl):
    _write_tmpl('/templates/add_product.html')

def salvar_produto(_handler, nome, descricao, preco, imagem):
    preco = float(preco)
    produto = Produto(nome=nome, descricao=descricao, preco=preco, imagem=imagem)
    produto.max_id()
    produto.put()

def editar_produto(id, nome, imagem, preco):
    produto = Produto.query(Produto.id == id).get()
    produto.nome = nome
    produto.imagem = imagem
    produto.preco = float(preco)
    produto.put()

def remover_produto(id):
    produto = Produto.query(Produto.id == id).get()
    produto.key.delete()
