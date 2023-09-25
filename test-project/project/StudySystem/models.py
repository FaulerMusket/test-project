from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=100)
    duration_seconds = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watched_duration = models.IntegerField(default=0)
    is_watched = models.BooleanField(default=False)

    #eighty_percents = duration_seconds / 100 * 80
    #if watched_duration >= eighty_percents:
    #    is_watched = models.BooleanField(True)
    #else:
    #    is_watched = models.BooleanField(False)

class Product(models.Model):
    owner = models.CharField(max_length=100)  
    name = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson)


class AccesToProduct(models.Model):
    Products = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)