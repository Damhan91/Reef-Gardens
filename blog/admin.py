from django.contrib import admin
from . models import Blogs


class BlogsAdmin(admin.ModelAdmin):
    """ Admin view for Blog Posts """
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('title', 'created')
