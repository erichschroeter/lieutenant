from django.contrib import admin

from entries.models import Entry, EntryTag

from favorites.models import Favorite

class EntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    list_filter = ['created_at']

admin.site.register(Entry, EntryAdmin)
admin.site.register(EntryTag)
admin.site.register(Favorite)
