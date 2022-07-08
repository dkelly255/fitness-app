# Credits: This code is sourced & adapted from the
# Code Institute Boutique Ado Project
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'),
]
