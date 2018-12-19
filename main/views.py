from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .forms import LoginForm
from .forms import RegistrationForm

from .models import Role
from .models import User

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponse("OK")
        else:
            return HttpResponse("Not found user with this login")    


class RegistrationView(TemplateView):
    template_name = 'reg.html'

    def post(self, request, *args, **kwargs):
        user = RegistrationForm(request.POST)
        new_user = user.save(commit=False)
        new_user.set_password(new_user.password)
        role = Role.objects.get(name='user')
        new_user.save()
        new_user.roles.add(role)
        new_user.save()
        return HttpResponse("OK")


class LogoutView(TemplateView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

class ListUserView(TemplateView):

    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context