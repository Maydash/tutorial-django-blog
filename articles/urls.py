from django.urls import path
from .views import ArticleListCreateAPIView, ArticleDetailView

urlpatterns = [

    path("articles/", ArticleListCreateAPIView.as_view()),
    path("articles/<int:id>/", ArticleDetailView.as_view()),


]


