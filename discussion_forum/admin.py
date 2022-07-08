from django.contrib import admin
from .models import Topic, Comment, Reply


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'author',
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


class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'reply_date',
        'author',
        'content',
        'comment',
    )

    ordering = ('reply_date',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
