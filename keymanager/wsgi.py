"""
WSGI config for keymanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/opt/keymanager/')
sys.path.append('/opt/keymanager/keymanager/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keymanager.settings")

application = get_wsgi_application()
