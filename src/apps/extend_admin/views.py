import re

from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import redirect
from django.contrib import messages

from .lib import send_invite, is_superuser


class IndexView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'extend_admin/index.html'
    login_url = 'admin:login'

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(is_superuser)
def send_invite_view(request):
    email = request.POST.get('email', '')
    if not re.match(r'.+@.+\..+', email):
        messages.error(request, 'You input not valid email.')
        return redirect('extend_admin_main')
    try:
        send_invite(email)
    except Exception as e:
        messages.error(request, str(e))
    else:
        messages.success(request, 'On email {} sent invite code.'.format(email))
    return redirect('extend_admin_main')
