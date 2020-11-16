from __future__ import absolute_import, unicode_literals

from realizestuff.celery import app
from django.core.mail import send_mail
import requests
import json

@app.task()
def send_password_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
    )