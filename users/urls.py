from django.urls import path

from users.views import LoginEmailView

urlpatterns = [
    path("login/", LoginEmailView.as_view(), name='login')
]
