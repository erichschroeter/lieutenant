from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from entries.models import Entry

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class EntryList(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['text', 'tags']
    template_name_suffix = '_form'

class EntryRead(LoginRequiredMixin, DetailView):
    model = Entry
    template_name_suffix = '_detail'

class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name_suffix = '_update_form'

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entries:index')
