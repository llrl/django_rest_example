from rest_framework import serializers
from main.models import User
from main.models import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'roles')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name')