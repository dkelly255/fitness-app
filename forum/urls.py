from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='forum'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]