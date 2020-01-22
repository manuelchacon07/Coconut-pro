import sys, os, bottle
import beaker.middleware

import coconut # Import coconut.py

sys.path = ['/var/www/coconut/'] + sys.path
os.chdir(os.path.dirname(__file__))

# Inicialice app with SessionMiddleware environ
application = beaker.middleware.SessionMiddleware(bottle.default_app(), coconut.session_opts)

