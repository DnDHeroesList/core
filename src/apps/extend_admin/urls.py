from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import IndexView, send_invite_view


urlpatterns = [
    url(r'^extend_admin_main$', IndexView.as_view(), name='extend_admin_main'),
    url(r'^send_invite', send_invite_view, name='send_invite')
]
