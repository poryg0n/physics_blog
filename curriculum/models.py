from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
#   name_tag = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    due_date = models.IntegerField(default=2020)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    attached_file = models.FileField(null=True, blank=True, upload_to="files/")


    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
#       return reverse('home')
