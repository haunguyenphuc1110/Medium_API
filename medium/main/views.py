from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from taggit.models import Tag
from rest_framework.permissions import IsAdminUser


class IsAdmindNotGet(IsAdminUser):
    """
    If request == get >  >  > just request = get not authen, other request must admin
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(IsAdmindNotGet, self).has_permission(request, view)


class PostList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdmindNotGet, )


class PostDetail(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer


class CommentList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAdmindNotGet, )


class CommentDetail(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAdmindNotGet, )


class TagList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
