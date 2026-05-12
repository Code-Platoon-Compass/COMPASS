from django.contrib import admin
from .models import Link
 
 
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'created_at', 'updated_at')
    search_fields = ('label', 'url')
    ordering = ('-created_at',)
 