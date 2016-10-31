from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class IndexView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'extend_admin/index.html'
    login_url = 'admin:login'

    def test_func(self):
        return self.request.user.is_superuser
