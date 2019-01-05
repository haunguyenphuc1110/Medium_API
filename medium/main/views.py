from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class PostList(viewsets.GenericViewSet,generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer