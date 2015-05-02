from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from entries.models import Entry

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class EntryList(ListView):
    model = Entry

class EntryCreate(CreateView):
    model = Entry
    fields = ['text', 'tags']
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
