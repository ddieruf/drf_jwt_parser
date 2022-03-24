from __future__ import absolute_import, unicode_literals

from restdemo.celery import app

from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from .models import User
import time

@app.task
def confirm_email(userpk):
    user = User.objects.get(pk=userpk)
    email_subject = 'Activate your account.'
    email_body = f'http://127.0.0.1:8000/api/auth/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}/'
    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@scraper.com',
        [user.email],
    )
    time.sleep(25)
    email.send(fail_silently=False)