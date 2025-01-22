# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView


# For login and logout, we can use Django’s built-in auth views directly.
# We’ll also add the route for our RegisterView.

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
