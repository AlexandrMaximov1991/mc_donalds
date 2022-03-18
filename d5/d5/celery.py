import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd5.settings')

app = Celery('d5')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
