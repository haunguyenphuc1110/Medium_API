from .models import * 
from rest_framework import serializers
from taggit.models import Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 
        depth = 1       

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1
 