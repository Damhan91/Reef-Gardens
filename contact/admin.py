from django.contrib import admin
from .models import Contact


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin view for messages sent to ContactUs
    """
    list_display = ('name', 'email', 'subject', 'created')
    search_fields = ('name', 'email', 'subject', 'body')
    list_filter = ('name', 'email')