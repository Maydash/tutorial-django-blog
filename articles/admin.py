from django.contrib import admin
from .models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title",)


admin.site.register(Article, ArticleAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "dob",)
    search_fields = ("first_name", "last_name",)
    list_filter = ("first_name", "dob",)


admin.site.register(Author, AuthorAdmin)
