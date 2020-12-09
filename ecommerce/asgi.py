"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
path_dotenv = Path('.') / '.env'
load_dotenv(dotenv_path=path_dotenv)

application = get_asgi_application()
