# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Usuario

def index(_write_tmpl):
    _write_tmpl('/templates/index.html')

def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)