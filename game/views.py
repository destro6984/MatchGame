from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

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


class GameUpdateView(LoginRequiredMixin, View):
    form_class = AddGameForm

    def get_object(self):
        return get_object_or_404(Game, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('game', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        return render(request, 'game/game_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if "joingame" in request.POST:
            game = self.get_object()
            game.participants.add(request.user)
            return redirect('game', pk=kwargs['pk'])
        elif "leftgame" in request.POST:
            game = self.get_object()
            game.participants.remove(request.user)
            return redirect('game', pk=kwargs['pk'])
        if form.is_valid():
            form.save()
            return redirect('game', pk=kwargs['pk'])


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
