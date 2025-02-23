from django.apps import AppConfig
import sys


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'
    def ready(self):
        # This prevents the scheduler from running twice when using the runserver command with auto-reload
        if 'runserver' in sys.argv:
            from .scheduler import start_scheduler
            start_scheduler()