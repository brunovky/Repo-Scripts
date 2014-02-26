#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class CalculadoraHandler(webapp2.RequestHandler):
    def get(self):
        num1 = int(self.request.get('num1'))
        num2 = int(self.request.get('num2'))
        op = int(self.request.get('op'))
        if op < 1 or op > 4:
            self.response.write('Operacao invalida')
        elif op == 1:
            self.response.write('Resultado: %s' %(num1 + num2))
        elif op == 2:
            self.response.write('Resultado: %s' %(num1 - num2))
        elif op == 3:
            self.response.write('Resultado: %s' %(num1 * num2))
        elif op == 4:
            self.response.write('Resultado: %s' %(num1 / num2))

class RedirectHandler(webapp2.RedirectHandler):
    def get(self):
        self.redirect('/resp')

app = webapp2.WSGIApplication([
    ('/calc', CalculadoraHandler),
    ('/redirect', RedirectHandler)
], debug=True)
