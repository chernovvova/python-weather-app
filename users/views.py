from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    template_name = 'users/signin.html'
    form_class = LoginUserForm

    success_url = reverse_lazy('weather:index')

    extra_context = {
        'title': 'Sign In',
    }


class RegisterUser(CreateView):
    template_name = 'users/signup.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('users:signin')

    extra_context = {
        'title': 'Sign Up',
    }