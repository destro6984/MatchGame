from django.urls import path

from users.views import LoginEmailView, LogoutView, SingUpView

urlpatterns = [
    path("login/", LoginEmailView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SingUpView.as_view(), name='register')
]
