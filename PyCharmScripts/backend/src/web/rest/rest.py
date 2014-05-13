# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    id = ndb.StringProperty()
    nome = ndb.StringProperty()
    email = ndb.StringProperty()
    admin = ndb.BooleanProperty()

class Produto(ndb.Model):
    id = ndb.IntegerProperty()
    nome = ndb.StringProperty()
    descricao = ndb.StringProperty()
    preco = ndb.FloatProperty()
    imagem = ndb.StringProperty()

    def max_id(self):
        produto =  self.query().order(-Produto.id).get()
        if produto:
            self.id = int(produto.id) + 1
        else:
            self.id = 1