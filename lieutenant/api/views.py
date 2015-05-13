from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from entries.models import Entry
from entries.serializers import EntrySerializer

from api.permissions import IsOwner

class EntryMixin(object):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (IsOwner,)

    def pre_save(self, obj):
        obj.user = self.request.user

class EntryList(EntryMixin, ListCreateAPIView):
    pass

class EntryDetail(EntryMixin, RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'

