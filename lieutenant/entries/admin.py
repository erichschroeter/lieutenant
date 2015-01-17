from django.contrib import admin

from entries.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    list_filter = ['created_at']

admin.site.register(Entry, EntryAdmin)
