from django.http import HttpResponse
from django.template import RequestContext, loader

from entries.models import Entry

def index(request):
    entries_list = Entry.objects.order_by('-created_at')[:5]
    template = loader.get_template('entries/index.html')
    context = RequestContext(request, {
        'entries_list': entries_list,
    })
    return HttpResponse(template.render(context))
