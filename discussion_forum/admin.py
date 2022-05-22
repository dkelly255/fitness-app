from django.contrib import admin
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
    )

    ordering = ('date_created',)


# Register your models here.
admin.site.register(Topic, TopicAdmin)