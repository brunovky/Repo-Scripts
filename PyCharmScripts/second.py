import webapp2

class ReceiveHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Fui redirecionado!')

app = webapp2.WSGIApplication([
    ('/resp', ReceiveHandler)
], debug=True)