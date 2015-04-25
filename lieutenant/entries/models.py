from django.db import models

from taggit.managers import TaggableManager

class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    tags = TaggableManager(blank=True)
    text = models.TextField(blank=True)
