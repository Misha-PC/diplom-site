from app import app
from app import db
import view
import api_routers

'''
from OpenSSL import SSL


context = SSL.Context(SSL.PROTOCOL_TLS)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')
'''

if __name__ == "__main__":
    # app.run(ssl_context=context)
    app.run()
