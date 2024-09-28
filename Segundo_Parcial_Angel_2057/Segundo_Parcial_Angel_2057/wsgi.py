"""
WSGI config for Segundo_Parcial_Angel_2057 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Segundo_Parcial_Angel_2057.settings')

application = get_wsgi_application()
