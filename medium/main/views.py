from django.contrib.auth.models import User
from django.http import JsonResponse

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


# All Category 1 IDs and names
class Category_1(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate1_id", "cate1_name").distinct()
    serializer_class = Category_1_Serializer


# Top 10 of cate 1 id
class Category_1_top10(APIView):
    queryset = Products.objects.all()

    def get(self, request, cate1_id, format=None):
        catObjList = Category.objects.filter(cate1_id=cate1_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = self.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)
        # print("listProductInfo: ", listProductInfo)

        # products = [
        #     product.product_id
        #     for product in Products.objects.filter(status=200).order_by("-value_count")[
        #         :100
        #     ]
        # ]

        # return Response(products)
        return Response(serializer.data)

    def get_product_from_cate3_new(self, inputID):
        tempSet = CateProduct.objects.filter(cate3_id_new=inputID).all()
        return list(map(lambda x: x.product_id, tempSet))

    def getAllProduct_fromListCate3(self, inputID_list):
        returnArr = []
        for i in inputID_list:
            returnArr += self.get_product_from_cate3_new(i)
        return returnArr


# class SessionViewSet(viewsets.ModelViewSet):
#     queryset = Session.objects.all()
#     serializer_class = SessionSerializer

#     def get(self, request, format=None):
#         return Response("test")


# class TopCat1(APIView):
#     def get(self, request, format=None):
#         return Response("hello world")


# class Cate1_Product(viewsets.GenericViewSet, generics.ListCreateAPIView):
#     queryset = CateProduct.objects.filter(cate3_new_id.cate1_id=1108)
