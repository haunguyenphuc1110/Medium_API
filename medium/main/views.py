from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from taggit.models import Tag
from rest_framework.permissions import IsAdminUser
from . import documents
from elasticsearch_dsl.query import MultiMatch

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# class IsAdmindNotGet(IsAdminUser):
#     """
#     If request == get >  >  > just request = get not authen, other request must admin
#     """

#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return True
#         return super(IsAdmindNotGet, self).has_permission(request, view)


# class PostList(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     # permission_classes = (IsAdmindNotGet, )
#     keyword_fields = ['title',
#                       'slug',
#                       'body',
#                       'publish', ]

#     def get_queryset(self):
#         qs = self.request.query_params.get('q', None)
#         if qs is None:
#             return self.queryset

#         words = qs.split(',')
#         search = documents.PostDocument.search()
#         match = MultiMatch(query=' '.join(
#             words), fields=self.keyword_fields, type='best_fields')
#         # q = Q('nested', path='skills', query=Q('match', skills__name=qs)) | Q(match)
#         search = search.query(match)
#         return search.to_queryset()


# class PostDetail(viewsets.GenericViewSet,
#                  generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer


# class CommentList(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAdmindNotGet, )


# class CommentDetail(viewsets.GenericViewSet,
#                     generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = (IsAdmindNotGet, )


# class TagList(viewsets.GenericViewSet,
#               generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


class CategoryList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Products.objects.filter(status=200)
    serializer_class = ProductSerializer


class UserList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class CateProductList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = CateProduct.objects.all()
    serializer_class = CateProductSerializer


class PopularityList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Products.objects.filter(status=200).order_by("-value_count")[:100]
    serializer_class = ProductSerializer


class Category_1(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate1_id", "cate1_name").distinct()
    serializer_class = Category_1_Serializer


# class TopCat1(APIView):
#     def get(self, request, format=None):
#         return Response("hello world")


# class Cate1_Product(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = CateProduct.objects.filter(cate3_new_id.cate1_id=1108)
