"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# import os
from dotenv import load_dotenv
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings'
path_dotenv = Path('.') / '.env'
load_dotenv(dotenv_path=path_dotenv)

application = get_wsgi_application()
