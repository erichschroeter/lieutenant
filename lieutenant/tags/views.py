from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from entries.models import EntryTag, TaggedEntry

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class TagList(LoginRequiredMixin, ListView):
    model = EntryTag

    def get_queryset(self):
        # get all tags
        queryset = EntryTag.objects.all()
	for tag in queryset:
	    count = len(TaggedEntry.objects.filter(tag__name=tag.name))
	    tag.count = count
        return queryset

class TagRead(LoginRequiredMixin, DetailView):
    model = EntryTag
    template_name_suffix = '_detail'

    def get_context_data(self, **kwargs):
        context = super(TagRead, self).get_context_data(**kwargs)
	count = len(TaggedEntry.objects.filter(tag=self.object.name))
	context.update({ 'count': count })
	return context

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = EntryTag
    template_name_suffix = '_update_form'
    fields = ['name', 'wiki']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
	context = self.get_context_data(object=self.object)
        return super(TagUpdate, self).get(request, *args, **kwargs)

class TagDelete(LoginRequiredMixin, DeleteView):
    model = EntryTag
    success_url = reverse_lazy('tags:index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
