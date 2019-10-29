from django.db import models

class FeedSource(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    url = models.CharField(max_length=200)
    interval = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class FeedInfo(models.Model):
    class Meta:
        verbose_name_plural = "Feed info"

    feed = models.OneToOneField('FeedSource', on_delete=models.CASCADE, related_name='info_of')
    guid = models.CharField(max_length=250)
    entry = models.TextField()
    updated = models.DateTimeField()

class FeedEntry(models.Model):
    class Meta:
        verbose_name_plural = "Feed entries"

    source = models.ForeignKey('FeedSource', on_delete=models.CASCADE)
    guid = models.CharField(max_length=250)
    entry = models.TextField()
    updated = models.DateTimeField()