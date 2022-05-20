from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'date_submitted',
        'email',
        'subject',
        'message',
    )

    ordering = ('date_submitted',)

admin.site.register(Contact, ContactAdmin)