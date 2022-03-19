import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd5.settings')

app = Celery('d5')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'board.tasks.clear_board',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks()

