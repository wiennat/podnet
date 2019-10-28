from django.db import models

# Create your models here.
class FeedSource(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    url = models.CharField(max_length=200)
    interval = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class FeedEntry(models.Model):
    source = models.ForeignKey('FeedSource', on_delete=models.CASCADE)
    guid = models.CharField(max_length=250)
    entry = models.TextField()
    updated = models.DateTimeField()