# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Usuario

def login(_write_tmpl):
    usuario = Usuario(login='bruno', pwd='br111092', logged=False)
    usuario.put()
    _write_tmpl('/templates/login.html')

def efetuar_login(_handler, _write_tmpl, login, pwd):
    msg = ''
    if login == '':
        msg = 'Login é obrigatório'
    elif pwd == '':
        msg = 'Senha é obrigatório'
    query = Usuario.query(Usuario.login == login, Usuario.pwd == pwd)
    if query.fetch():
        usuario = query.get()
        setattr(usuario, 'logged', True)
        usuario.put()
        _handler.redirect('/')
    else:
        if msg == '':
            msg = 'Login e/ou senha inválidos'
        dict = {
            'login_error':True,
            'msg_error': msg
            }
        _write_tmpl('/templates/login.html', dict)