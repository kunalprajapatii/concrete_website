from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('first_name', 'email', 'subject')
