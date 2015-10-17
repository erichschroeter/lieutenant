from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from entries.models import Entry, EntryTag
from entries.serializers import EntrySerializer, EntryTagSerializer

from api.permissions import IsOwner

class EntryMixin(object):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (IsOwner,)

    def pre_save(self, obj):
        obj.user = self.request.user

class EntryList(EntryMixin, ListCreateAPIView):
    def get_queryset(self):
        """
        This view should return a list of entries determined by the
        date specified in the URL.
        """
        if 'day' in self.kwargs:
            year = self.kwargs['year']
            month = self.kwargs['month']
            day = self.kwargs['day']
            return Entry.objects.filter(created_at__year=year, created_at__month=month, created_at__day=day)
        elif 'month' in self.kwargs:
            year = self.kwargs['year']
            month = self.kwargs['month']
            return Entry.objects.filter(created_at__year=year, created_at__month=month)
        elif 'year' in self.kwargs:
            year = self.kwargs['year']
            return Entry.objects.filter(created_at__year=year)

        return Entry.objects.all()

class EntryDetail(EntryMixin, RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'

class TagsList(ListCreateAPIView):
    serializer_class = EntryTagSerializer

    def get_queryset(self):
        if 'filter' in self.kwargs:
            tagfilter = self.kwargs['filter']
            return EntryTag.objects.filter(name__startswith=tagfilter)
        return EntryTag.objects.all()
