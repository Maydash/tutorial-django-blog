from rest_framework import serializers
from .models import Article, Author
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email",)


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name")


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ("id", "title", "content", "created_at")
