from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='article/')
    price = models.FileField(upload_to='price/')



