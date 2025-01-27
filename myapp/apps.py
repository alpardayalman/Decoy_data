from django.apps import AppConfig
import threading
from .tasks import add_sample_data

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        threading.Thread(target=add_sample_data, daemon=True).start()
