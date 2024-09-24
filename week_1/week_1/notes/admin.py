from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at', 'user']
    search_fields = ['title', 'description', 'user']
    list_filter = ('created_at', 'user')
