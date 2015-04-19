from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from entries.models import Entry

class EntryList(ListView):
    model = Entry

class EntryCreate(CreateView):
    model = Entry
    template_name_suffix = '_form'

class EntryRead(DetailView):
    model = Entry
    template_name_suffix = '_detail'

class EntryUpdate(UpdateView):
    model = Entry
    template_name_suffix = '_update_form'

class EntryDelete(DeleteView):
    model = Entry
    success_url = reverse_lazy('entries:index')
