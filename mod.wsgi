import os
import sys

sys.path.insert(0, '/home/f/fr7913td/voie.tk/public_html/studmash/')
sys.path.insert(0, '/home/f/fr7913td/voie.tk/public_html/studmash/studmash/')
sys.path.insert(0, '/home/f/fr7913td/voie.tk/public_html/env/lib/python2.7/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'studmash.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
