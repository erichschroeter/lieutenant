from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import TagBase, ItemBase, TaggedItemBase, GenericTaggedItemBase

from randomslugfield import RandomSlugField

class EntryTag(TagBase):
    wiki = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class TaggedEntry(GenericTaggedItemBase):
    tag = models.ForeignKey(EntryTag, related_name="%(app_label)s_%(class)s_items")

class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey('auth.User', related_name='entries')
    # 62 possible chars ^ 5 length = 916,132,832 possible slugs
    slug = RandomSlugField(length=5)
    tags = TaggableManager(blank=True, through=TaggedEntry)
    text = models.TextField(blank=True)
