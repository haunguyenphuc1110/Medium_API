from .models import *
from rest_framework import serializers
from taggit.models import Tag

# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

# from main import documents as articles_documents


# class PostDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = articles_documents.PostDocument
#         fields = (
#             'id',
#             'title',
#             'body',
#             'author',
#             'created',
#             'modified',
#             'pub_date',
#         )
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         depth = 1


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         depth = 1


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'
#         depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        depth = 1


class CateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CateProduct
        fields = "__all__"
        depth = 2


# ----------------ALL CATEGORY CLASS---------
# All Category 1
class Category_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_1
        fields = "__all__"
        depth = 1


# All Category 2
class Category_2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_2
        fields = "__all__"
        depth = 1


class Category_3_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_3
        fields = "__all__"
        depth = 1


# -----------END OF CATEGORY CLASS##

# ----------SUB CATEGORY-------------
# ---------END OF SUB CATEGORY------

# -----LOGIN SERIALIZE-----------
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("user_id", "last_activity", "mac_address")
        depth = 1
