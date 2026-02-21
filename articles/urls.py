from django.urls import path
from .views import ArticleListCreateAPIView, ArticleDetailView, AuthorListCreateAPIView, AuthorDetailAPIView, UserMeView

urlpatterns = [
    path("users/me/", UserMeView.as_view()),
    path("articles/", ArticleListCreateAPIView.as_view()),
    path("articles/<int:id>/", ArticleDetailView.as_view()),

    path("authors/", AuthorListCreateAPIView.as_view()),
    path("authors/<int:id>/", AuthorDetailAPIView.as_view()),
]


