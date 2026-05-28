import os
from django.core.wsgi import get_wsgi_application

# On pointe bien vers les settings de ton dossier project_config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')

application = get_wsgi_application()