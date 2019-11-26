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


<<<<<<< HEAD
# ----------------ALL CATEGORY CLASS---------
# All Category 1
=======
# Category 1
>>>>>>> 70d846f4e5014d195e17b9a591a1a1fa9df25b95
class Category_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_1
        fields = "__all__"
<<<<<<< HEAD
        depth = 1


# All Category 2
class Category_2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_2
        fields = "__all__"
=======
>>>>>>> 70d846f4e5014d195e17b9a591a1a1fa9df25b95
        depth = 1


class Category_3_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_3
        fields = "__all__"
        depth = 1


# -----------END OF CATEGORY CLASS

# ----------SUB CATEGORY-------------
class CategoryFilter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


# ---------END OF SUB CATEGORY------
