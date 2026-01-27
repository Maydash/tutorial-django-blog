from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title",)


admin.site.register(Article, ArticleAdmin)




