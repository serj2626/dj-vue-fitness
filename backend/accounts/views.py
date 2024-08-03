from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

