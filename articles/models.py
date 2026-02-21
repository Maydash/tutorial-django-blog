from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="articles", null=True, blank=True)


# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
#     parent = models.ForeignKey(
#         "self",
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#         related_name="replies"
#     )
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.id} - {self.article.title}"
#

class Comment(MPTTModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["crated_at"]



