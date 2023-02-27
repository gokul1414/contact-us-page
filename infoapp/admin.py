from django.contrib import admin
from .models import ContactDatas

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')

admin.site.register(ContactDatas)