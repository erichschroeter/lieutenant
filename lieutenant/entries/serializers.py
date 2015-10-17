from django.forms import widgets

from rest_framework import serializers

from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

from entries.models import Entry, EntryTag

class EntrySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Entry
        fields = ('slug', 'created_at', 'updated_at', 'text', 'tags')

class EntryTagSerializer(serializers.ModelSerializer):

    class Meta:
	model = EntryTag
	fields = ('name', 'wiki')
