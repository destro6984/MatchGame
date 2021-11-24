from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from actions.models import Action
from game.models import Game
from users.forms import LoginForm, SignUpForm, EditUserForm
from users.models import User


# SuccessMessageMixin


class LoginEmailView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_field_name = 'home'
    redirect_authenticated_user = True
    # success_message=f'Welcome'


class LogoutView(auth_views.LogoutView):
    template_name = "users/logout.html"



class SingUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'users/registration_form.html'


class UserDetailView(DetailView):
    model = User
    context_object_name = 'player'
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['actions'] = Action.objects.filter(user_id=self.object.id)[:5]
        context['games'] = self.object.games.all
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'users/update-user.html'
    success_url = reverse_lazy('home')
