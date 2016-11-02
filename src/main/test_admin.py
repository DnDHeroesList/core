from django.contrib.auth.models import User
from django.test import Client

import pytest


@pytest.fixture()
def create_users():
    User.objects.create_superuser(username='test_user', email='test@test.com', password='password')


def test_login_200():
    c = Client()
    c = c.get('/admin/login/')
    assert c.status_code == 200


@pytest.mark.django_db()
def test_after_login_200(create_users):
    c = Client()
    c.login(username='test_user', password='password')
    c = c.get('/admin/', follow=True)
    assert c.status_code == 200
    assert c.context[0]['user'].username == 'test_user'
