"""
WSGI config for TupcOnlineSys project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import time


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TupcOnlineSys.settings')
os.environ["TZ"] = "Asia/Hong_Kong"
time.tzset()
application = get_wsgi_application()
