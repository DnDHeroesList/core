from django.test import Client


def test_200():
    c = Client()
    c = c.get('/')
    assert c.status_code == 200
    assert 'Привет' in c.content.decode('utf-8')
