from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'date_submitted',
        'first_name',
        'last_name',
        'email',
        'subject',
        'message',
    )

    ordering = ('date_submitted',)

admin.site.register(Contact, ContactAdmin)
