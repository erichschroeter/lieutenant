from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from django.shortcuts import redirect

from entries.models import Entry

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class Home(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        return redirect('/entries/')

