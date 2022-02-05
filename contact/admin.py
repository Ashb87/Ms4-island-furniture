from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Creates data list for admin """
    list_display = ('email_date', 'query', 'user')
    ordering = ('-email_date', 'user',)


admin.site.register(Contact, ContactAdmin)
