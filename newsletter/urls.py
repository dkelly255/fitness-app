from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
]