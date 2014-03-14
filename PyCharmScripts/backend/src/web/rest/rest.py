# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    login = ndb.StringProperty()
    pwd = ndb.StringProperty()
    logged = ndb.BooleanProperty()

def logar(login, pwd):
    query = Usuario.query(Usuario.login == login, Usuario.pwd == pwd)
    if query.fetch():
        usuario = query.get()
        setattr(usuario, 'logged', True)
        usuario.put()
        return True
    return False