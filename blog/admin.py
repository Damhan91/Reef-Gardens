from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    """ Admin view for Blog Posts """
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('title', 'created')
    summernote_fields = ('body')