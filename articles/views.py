from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


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




