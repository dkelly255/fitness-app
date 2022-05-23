from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_screen, name='discussion_forum'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('edit_topic/<topic_id>', views.edit_topic, name='edit_topic'),
    path('delete_topic/<topic_id>', views.delete_topic, name='delete_topic'),
    path('add_comment/<topic_id>', views.add_comment, name='add_comment'),
    path('delete_comment/<comment_id>', views.delete_comment, name='delete_comment'),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
    path('reply_to_comment/<comment_id>', views.reply_to_comment, name='reply_to_comment'),
    path('delete_reply/<reply_id>', views.delete_reply, name='delete_reply'),
]