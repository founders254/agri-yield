from django.urls import path
from .views import register_page, login_page, register_user, login_user

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('api/accounts/register/', register_user, name='register'),
    path('api/accounts/login/', login_user, name='login'),
]