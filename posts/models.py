from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the post is updated

    def __str__(self):
        return self.title
