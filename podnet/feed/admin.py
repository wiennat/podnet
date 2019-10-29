from django.contrib import admin

# Register your models here.
from .models import FeedSource, FeedEntry, FeedInfo


class FeedSourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'slug']}),
        ('Fetch configuration', {'fields': ['url', 'interval']}),
    ]

admin.site.register(FeedSource, FeedSourceAdmin)
admin.site.register(FeedEntry)
admin.site.register(FeedInfo)