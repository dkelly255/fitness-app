from django.contrib import admin
from .models import Topic, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
    )

    ordering = ('date_created',)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_date',
        'author',
        'content',
        'topic',   
    )

    ordering = ('comment_date',)

# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)