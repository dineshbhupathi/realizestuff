from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realizestuff.settings')
app = Celery('realizestuff')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduledemails.settings')
#
# app = Celery('scheduledemails',broker='amqp://localhost')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
#

app.conf.beat_schedule = {
     'bulkdeittonormaluser': {
         'task': 'salesforcedjango.djangosalesforceauth.tasks.send_bulkdeittonormalusertipsemail',
         'schedule':crontab(minute=0, hour='3'),

     },
 'bulkdietandactivity': {
         'task': 'salesforcedjango.djangosalesforceauth.tasks.send_bulkhealthtipsemail',
         'schedule':crontab(minute=0, hour='3'),

     },
 }

app.conf.timezone = 'Asia/Kolkata'