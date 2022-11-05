from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class Ebook(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    cover_urls=models.CharField(max_length=2048)

    def __str__(self):
     return self.title

class Cart_Items(models.Model):
    title=models.CharField(max_length=50,null=True)
    price=models.FloatField(null=True)