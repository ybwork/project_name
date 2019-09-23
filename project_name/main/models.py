from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=30)
    status = models.CharField(max_length=20)



