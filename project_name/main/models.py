from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=30)
    status = models.CharField(max_length=20)


class Display(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    page = models.CharField(max_length=100)


class Images(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article')



