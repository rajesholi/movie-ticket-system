"""
WSGI config for movie_ticket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_ticket.settings')

# Django's default variable
application = get_wsgi_application()

# Add this line explicitly so Vercel can find the entry point
app = application