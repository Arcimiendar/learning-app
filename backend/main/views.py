from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegistrationForm


class LoginView(auth_views.LoginView):
    template_name = 'main/login.html'
    # redirect_authenticated_user = reverse_lazy('index')


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class RegistrationView(FormView):
    template_name = 'main/registration.html'
    model = get_user_model()
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # make creation of user
        return super().form_valid(form)

