from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

from artists.models import HistorySearch
from .forms import RegistrationForm
from .models import UserProfile
from .mixins import LoginRequiredMixin


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/profile/'

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/profile/'

    def form_valid(self, form):
        user = form.cleaned_data
        UserProfile.create_user_with_profile(user)
        user_login = authenticate(username=user['username'], password=user['password'])
        if user_login is not None:
            if user_login.is_active:
                login(self.request, user_login)
        return super(RegisterView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['history'] = HistorySearch.get_distinct_historial(self.request.user)
        return context
