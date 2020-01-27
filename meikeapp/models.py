from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class News(models.Model):
    url=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    uname = models.CharField(max_length=50)
    content=models.TextField()
    time=models.CharField(max_length=30)
    source=models.CharField(max_length=50)

class Admin(models.Model):
    uname = models.CharField(max_length=50)
    password=models.CharField(max_length=50)