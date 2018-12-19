from django.urls import path

from .views import LoginView
from .views import RegistrationView

urlpatterns = [
    path('', LoginView.as_view(), name='login_form'),
    path('login', LoginView.as_view(), name='login_form'),
    path('registration', RegistrationView.as_view(), name='registration_form')
]
