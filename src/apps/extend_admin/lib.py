import hashlib

from django.conf import settings
from django.core.mail import send_mail


def send_invite(email):
    hash = hashlib.sha224((settings.SECRET_KEY + email).encode('utf-8')).hexdigest()
    send_mail(
        'Invite code',
        'Your invite code: {}'.format(hash),
        settings.EMAIL,
        [email],
        fail_silently=False,
    )


def is_superuser(user):
    return user.is_superuser