from django.urls import path

from game.views import HomeView, GameCreate

urlpatterns = [
    path("create/", GameCreate.as_view(), name="create-game"),
]
