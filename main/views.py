from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.template import Template

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

def login(request):
    return render(request,'login.html')
