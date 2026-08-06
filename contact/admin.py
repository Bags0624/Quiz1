from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    list_filter = ('submitted_at',)