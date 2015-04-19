from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext, loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from entries.models import Entry

def index(request):
    entries_list = Entry.objects.order_by('-created_at')[:5]
    template = loader.get_template('entries/index.html')
    context = RequestContext(request, {
        'entries_list': entries_list,
    })
    return HttpResponse(template.render(context))

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
