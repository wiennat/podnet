from django.contrib import admin

# Register your models here.
from .models import FeedSource, FeedEntry

admin.site.register(FeedSource)
admin.site.register(FeedEntry)

