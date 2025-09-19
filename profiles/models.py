from django.db import models
from authors.models import Author

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    # To save the profile with name in the back end.
    def __str__(self): 
        return self.name

