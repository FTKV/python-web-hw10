from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=150, null=False, unique=True)
    born_date = models.DateField(null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=10000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.fullname}"
    

class Tag(models.Model):
    title = models.CharField(max_length=50, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"#{self.title}"
    

class Quote(models.Model):
    quote = models.CharField(max_length=10000, null=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.quote}"
