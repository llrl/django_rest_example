from django.urls import path
from django.contrib.auth.views import logout_then_login

from .views import LoginView
from .views import EditUserView
from .views import ListUserView
from .views import DeteleUserView
from .views import RegistrationView

urlpatterns = [
    path('', LoginView.as_view(), name='login_form'),
    path('login', LoginView.as_view(), name='login_form'),
    path('create_user', RegistrationView.as_view(), name='create_user_form'),
    path('list_users', ListUserView.as_view(), name='list_users'),
    path('list_users/<int:role_id>', ListUserView.as_view(), name='list_users'),
    path('edit_user/<int:id>', EditUserView.as_view(), name='edit_user'),
    path('delete_user/<int:id>', DeteleUserView.as_view(), name='delete_user'),
    path('logout', logout_then_login, name='logoutv')
]
