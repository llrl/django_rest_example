from django.urls import path
from django.contrib.auth.views import logout_then_login

from .views import LoginView
from .views import ListUserView
from .views import RegistrationView

urlpatterns = [
    path('', LoginView.as_view(), name='login_form'),
    path('login', LoginView.as_view(), name='login_form'),
    path('registration', RegistrationView.as_view(), name='registration_form'),
    path('list_users', ListUserView.as_view(), name='list_users'),
    path('logout', logout_then_login, name='logoutv')
]
