from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

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

#class EntryList(APIView):

    #def get(self, request, format=None):
	#entries = Entry.objects.all()
	#serializer = EntrySerializer(entries, many=True)
	#return Response(serializer.data)

    #def post(self, request, format=None):
	#serializer = EntrySerializer(data=request.data)
	#if serializer.is_valid():
	    #serializer.save()
	    #return Response(serializer.data, status=status.HTTP_201_CREATED)
	#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryRead(APIView):
    model = Entry

    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialize.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

