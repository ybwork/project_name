from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='article/', blank=True, null=True)
    # price = models.FileField(upload_to='price')



