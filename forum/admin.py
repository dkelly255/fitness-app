from django.contrib import admin
from .models import *
 
# Register your models here.
class DiscussionAdmin(admin.ModelAdmin):
    
    list_display = (
        'forum',
        'discuss',
    )

admin.site.register(forum)
admin.site.register(Discussion, DiscussionAdmin)