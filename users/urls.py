from django.urls import path

from users.views import LoginEmailView, LogoutView, SingUpView, UserDetailView, UserUpdateView

urlpatterns = [
    path("login/", LoginEmailView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SingUpView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
]
