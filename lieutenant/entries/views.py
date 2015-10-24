from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from favorites.models import Favorite

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

from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import redirect
from taggit.managers import TaggableManager

class EntryClone(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name_suffix = '_update_form'
    fields = ['text', 'tags']

    def get_object(self, queryset=None):
        clone = super(EntryClone, self).get_object(queryset)

        tags = clone.tags.names()

        # Clone the object specified by the URL slug
        clone.pk = None
        clone.slug = None
        clone.save()

        for tag in tags:
            clone.tags.add(tag)

        return clone

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Users should only be allowed to see their own entries
        if self.object.user == self.request.user:
            context = self.get_context_data(object=self.object)
            return redirect('/entries/update/' + self.object.slug)
        else:
            return HttpResponseForbidden()

class EntryFavoriteList(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Favorite.objects.favorites_of_user(self.request.user)

class EntryFavorite(LoginRequiredMixin, DetailView):
    model = Entry

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(Entry, slug=kwargs['slug'])

        # Users should only be allowed to see their own entries
        if self.object.user == self.request.user:
            fav = Favorite.objects.favorites_for_obj(self.object)
            # Toggle the favorite by creating or deleting the table entry
            if not fav:
                Favorite.objects.create_favorite(self.object.user, self.object)
            else:
                fav.delete()
            context = self.get_context_data(object=self.object)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseForbidden()

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
    fields = ['text', 'tags']

    def get_context_data(self, **kwargs):
       context = super(EntryUpdate, self).get_context_data(**kwargs)
       context.update({'is_update': True})
       return context

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
