from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from game.models import Game


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
    model = Game
    fields = ['stadium', 'price', 'max_players', 'date']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(GameCreate, self).form_valid(form)
