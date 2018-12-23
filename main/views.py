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
            return redirect('/list_users')
        else:
            return HttpResponse("Not found user with this login")


class RegistrationView(TemplateView):
    template_name = 'reg.html'

    def post(self, request, *args, **kwargs):
        user = RegistrationForm(request.POST)
        to_set_role = request.POST['role']
        new_user = user.save(commit=False)
        new_user.set_password(new_user.password)
        role = Role.objects.get(name=to_set_role)
        new_user.save()
        new_user.roles.add(role)
        new_user.save()
        return HttpResponse("OK")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        return context


class LogoutView(TemplateView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class ListUserView(TemplateView):

    template_name = 'user_list.html'

    def get(self, request, role_id=None):
        user = self.request.user
        if user.is_authenticated:
            return render(request, self.template_name, self.get_context_data(role_id=role_id))
        return redirect('/login')

    def get_context_data(self, role_id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['profile'] = user
        if role_id:
            users = User.objects.filter(roles__id=role_id)
        else:
            users = User.objects.all() 
        context['users'] = users
        context['is_superuser'] = user.is_superuser
        return context

class EditUserView(TemplateView):

    template_name = 'edit.html'

    def get(self, request, id):
        if request.user.is_authenticated:
            print(type(request.user))
            print(request.user)
            roles = request.user.roles.all()
            if 'admin' in roles:
                print("okey")
        return HttpResponse("OK")

    def get_context_data(self, **kwargs):
        print(**kwargs)
        return HttpResponse(**kwargs)
        

class DeteleUserView(TemplateView):

    def get(self, request, id):
        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            return HttpResponse("Your are not auth as superuser")
        user_to_del = User.objects.filter(id=id).first()
        if not user_to_del:
            return HttpResponse("User to delete not exist")
        user_to_del.delete()
        return HttpResponse("OK")
