from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name
