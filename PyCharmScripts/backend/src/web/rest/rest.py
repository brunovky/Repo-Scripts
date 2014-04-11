# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    nome = ndb.StringProperty()
    email = ndb.StringProperty()
    id = ndb.StringProperty()

class Produto(ndb.Model):
    nome = ndb.StringProperty()
    descricao = ndb.StringProperty()
    preco = ndb.FloatProperty()
    imagem = ndb.StringProperty()

def logar(login, pwd):
    query = Usuario.query(Usuario.login == login, Usuario.pwd == pwd)
    if query.fetch():
        usuario = query.get()
        setattr(usuario, 'logged', True)
        usuario.put()
        return True
    return False