# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from web.rest.rest import Usuario


def execute(next_process, handler, dependencies, **kwargs):
    user = users.get_current_user()
    if user:
        logged_user = Usuario.query(Usuario.id == user.user_id()).get()
        if not logged_user:
            logged_user = Usuario(nome=user.nickname(), email=user.email(), id=user.user_id())
            logged_user.put()
        dependencies['logged'] = True
        dependencies['username'] = logged_user.nome
        dependencies['_logout_url'] = users.create_logout_url('/')
    else:
        dependencies['logged'] = None
        dependencies['_login_url'] = users.create_login_url('/')
    next_process(dependencies, **kwargs)
