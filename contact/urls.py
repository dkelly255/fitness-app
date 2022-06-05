from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('enquiry_log/', views.enquiry_log, name='enquiry_log'),
    path('action_enquiry/<enquiry_id>', views.action_enquiry, name='action_enquiry'),
    path('newsletter/', views.newsletter, name='newsletter'),
]