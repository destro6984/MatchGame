from django.urls import path

from game.views import HomeView, GameCreate, StadiumCreate, GameDetailView, GameUpdateView, GameDeleteView

urlpatterns = [
    path("create/", GameCreate.as_view(), name="create-game"),
    path("create-stadium/", StadiumCreate.as_view(), name="create-stadium"),
    path("<int:pk>", GameDetailView.as_view(), name="game"),
    path("update/<int:pk>", GameUpdateView.as_view(), name="update-game"),
    path("delete/<int:pk>/", GameDeleteView.as_view(), name='delete-game'),
]
