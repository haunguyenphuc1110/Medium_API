import hashlib

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from taggit.models import Tag
from . import documents
from elasticsearch_dsl.query import MultiMatch

from . import utils

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


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
class CategoryList(viewsets.GenericViewSet, generics.ListCreateAPIView):
    # @method_decorator(cache_page(60*60*2))
    # @method_decorator(vary_on_cookie)
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


# -------------CATEGORY CLASS-------------------
# All Category 1 IDs and names
class Category_1(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate1_id", "cate1_name").distinct()
    serializer_class = Category_1_Serializer


# All Category 2 IDs and names
class Category_2(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate2_id", "cate2_name").distinct()
    serializer_class = Category_2_Serializer


class Category_3(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.order_by().values("cate3_id", "cate3_name").distinct()
    serializer_class = Category_3_Serializer


# -------------END OF CATEGORY CLASS----------------

# -----------SUB CATEGORY------------
class Category_1_2(viewsets.GenericViewSet, generics.ListCreateAPIView):
    queryset = (
        Category.objects.filter(cate1_id=1686)
        .values("cate2_id", "cate2_name")
        .distinct()
    )
    serializer_class = Category_2_Serializer


# ----------Top products of cate 1,2,3 id-----------
class Category_prod_1_top(APIView):
    # @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, cate1_id, format=None):
        catObjList = Category.objects.filter(cate1_id=cate1_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


class Category_prod_2_top(APIView):
    def get(self, request, cate2_id, format=None):
        catObjList = Category.objects.filter(cate2_id=cate2_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


class Category_prod_3_top(APIView):
    def get(self, request, cate3_id, format=None):
        catObjList = Category.objects.filter(cate3_id=cate3_id).all()
        list_cate3_id_new = list(map(lambda x: x.cate3_id_new, catObjList))
        listProductID = utils.getAllProduct_fromListCate3(list_cate3_id_new)
        listProductInfo = Products.objects.filter(
            pk__in=listProductID, status=200
        ).order_by("-value_count")[:100]

        products = [product.product_id for product in listProductInfo]
        serializer = ProductSerializer(listProductInfo, many=True)

        return Response(serializer.data)


# -------------End of top product of category---------

# -----------Top Children category of a category-------
class Category_cate_1_top(APIView):
    def get(self, request, cate1_id, format=None):
        cat1Obj = Category.objects.filter(cate1_id=cate1_id).all()
        cat2_id_list = list(set(map(lambda x: x.cate2_id, cat1Obj)))

        totalCountList = []

        for id_2 in cat2_id_list:
            sampleCat3_new = Category.objects.filter(
                cate1_id=cate1_id, cate2_id=id_2
            ).all()
            sampleCat3_list = list(map(lambda x: x.cate3_id_new, sampleCat3_new))
            totalCount = utils.getTotalValueCount_fromListCate3(sampleCat3_list)
            totalCountList.append(totalCount)

        return Response((dict(zip(cat2_id_list, totalCountList))))


class Category_cate_2_top(APIView):
    pass


# -------------------End of top Children category of a category

# -----------Category filter--------------
class CategoryFilter(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    # def get_serializer_class(self):
    #     print("IM IN THE SERIALIZE")

    #     cate1_id = self.request.query_params.get("cate1_id", None)
    #     cate2_id = self.request.query_params.get("cate2_id", None)

    #     if cate1_id is not None:
    #         if cate2_id is not None:
    #             serializer_class = Category_3
    #         else:
    #             serializer_class = Category_2
    #     elif cate2_id is not None:
    #         serializer_class = Category_3

    #     return serializer_class

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        print("IM IN THE QUERY SET")
        queryset = Category.objects.all()

        cate1_id = self.request.query_params.get("cate1_id", None)
        cate2_id = self.request.query_params.get("cate2_id", None)
        only_cate2 = self.request.query_params.get("only_cate2", None)

        # Rewrite code
        if cate1_id is not None:
            queryset = queryset.filter(cate1_id=cate1_id)
        if cate2_id is not None:
            queryset = queryset.filter(cate2_id=cate2_id)

        return queryset


class CategoryFilter_level2(generics.ListCreateAPIView):
    serializer_class = Category_2_Serializer

    def get_queryset(self):
        queryset = Category.objects.all()
        cate1_id = self.request.query_params.get("cate1_id", None)
        if cate1_id is not None:
            queryset = queryset.filter(cate1_id=cate1_id).distinct()
        return queryset


class CategoryFilter_level3(generics.ListCreateAPIView):
    serializer_class = Category_3_Serializer

    def get_queryset(self):
        queryset = Category.objects.all()
        cate2_id = self.request.query_params.get("cate2_id", None)
        if cate2_id is not None:
            queryset = queryset.filter(cate2_id=cate2_id).distinct()
        return queryset


# ----------_End of Category filter-------


# ---User Login View-----------=
class UserLogin(APIView):
    def get(self, request, username, password, format=None):
        hash_pass = hashlib.md5(password.encode()).hexdigest()
        user = Users.objects.filter(username=username).all()

        if user.first().password == hash_pass:
            serializer = UserLoginSerializer(user, many=True)
            return Response(serializer.data[0])
        return Response({"message": "login fail"})


# ---- User Filter------------
class UserFilter(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a user by user_id
        """
        queryset = Users.objects.all()

        user_id = self.request.query_params.get("user_id", None)

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


# -------End of user filter

# -----User history-----------
class UserHistory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a user by user_id
        """
        user_id = self.request.query_params.get("user_id", None)

        if user_id:
            users = Users.objects.get(user_id=user_id)
            queryset = Products.objects.filter(pk__in=users.history)

        return queryset


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
