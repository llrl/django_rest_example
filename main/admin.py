from django.contrib import admin

# Register your models here.
from .models import Role
from .models import User

admin.site.register(Role)
admin.site.register(User)