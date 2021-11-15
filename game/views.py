from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class HomeView(View):
    template_name = "game/home.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
