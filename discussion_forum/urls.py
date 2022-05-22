from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_screen, name='discussion_forum'),
    path('create_topic/', views.create_topic, name='create_topic'),
]