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
    nome = ndb.StringProperty()
    descricao = ndb.StringProperty()
    preco = ndb.FloatProperty()
    imagem = ndb.StringProperty()