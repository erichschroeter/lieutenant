from django.db import models

from taggit.managers import TaggableManager

from randomslugfield import RandomSlugField

class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey('auth.User', related_name='entries')
    # 62 possible chars ^ 5 length = 916,132,832 possible slugs
    slug = RandomSlugField(length=5)
    tags = TaggableManager(blank=True)
    text = models.TextField(blank=True)
