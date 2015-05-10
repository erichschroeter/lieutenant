from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

class EntryListByYear(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user, created_at__year=self.kwargs['year'])

class EntryListByMonth(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user, created_at__year=self.kwargs['year'], created_at__month=self.kwargs['month'])

class EntryListByDay(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user, created_at__year=self.kwargs['year'], created_at__month=self.kwargs['month'], created_at__day=self.kwargs['day'])

class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['text', 'tags']
    template_name_suffix = '_form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EntryCreate, self).form_valid(form)

class EntryRead(LoginRequiredMixin, DetailView):
    model = Entry
    template_name_suffix = '_detail'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Users should only be allowed to see their own entries
        if self.object.user == self.request.user:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden()

class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name_suffix = '_update_form'
    fields = ['text', 'tags']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Users should only be allowed to see their own entries
        if self.object.user == self.request.user:
            context = self.get_context_data(object=self.object)
            return super(EntryUpdate, self).get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entries:index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Users should only be allowed to see their own entries
        if self.object.user == self.request.user:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden()
