from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from game.forms import AddGameForm
from game.models import Game, Stadium


class HomeView(View):
    template_name = "game/home.html"

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        # games = Game.objects.filter(
        #     Q(topic__name__icontains=q) |
        #     Q(name__icontains=q) |
        #     Q(description__icontains=q)
        # )
        games = Game.objects.all()
        context = {'games': games}
        return render(request, self.template_name, context)


class GameCreate(CreateView):
    template_name = 'game/game_form.html'
    form_class = AddGameForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(GameCreate, self).form_valid(form)


class GameDetailView(DetailView):
    model = Game
    template_name = 'game/game.html'


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    # form_class = EditUserForm
    # template_name = 'users/update-user.html'
    success_url = reverse_lazy('home')


class GameDeleteView(DeleteView):
    model = Game


class StadiumCreate(CreateView):
    model = Stadium
    fields = ['city', 'address']
    template_name = 'game/stadium_form.html'
    # form_class = AddGameForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(StadiumCreate, self).form_valid(form)
