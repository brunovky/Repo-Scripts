# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Usuario

def index(_write_tmpl):
    dict = {}
    query = Usuario.query(Usuario.logged == True)
    if query.fetch():
        usuario = query.get()
        dict = {'logged': True,
                'username': usuario.login}
    else:
        dict = {'logged': False}
    _write_tmpl('/templates/index.html', dict)

def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)