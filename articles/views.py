from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class AuthorListCreateAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class AuthorDetailAPIView(APIView):

    def get(self, request, id):
        author = get_object_or_404(Author, id=id)
        serializers = ArticleSerializer(instance=author)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def put(self, request):
        author = get_object_or_404(Author, id=id)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        author = get_object_or_404(Author, id=id)
        serializer = ArticleSerializer(instance=author, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        author = get_object_or_404(Author, id=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListCreateAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailView(APIView):

    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        serializer = ArticleSerializer(instance=article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def put(self, request, id):
        article = get_object_or_404(Article, id=id)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def patch(self, request, id):
        article = get_object_or_404(Article, id=id)
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        article = get_object_or_404(Article, id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
