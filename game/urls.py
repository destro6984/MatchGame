from django.urls import path

from game.views import HomeView, GameCreate, StadiumCreate

urlpatterns = [
    path("create/", GameCreate.as_view(), name="create-game"),
    path("create-stadium/", StadiumCreate.as_view(), name="create-stadium"),
]
