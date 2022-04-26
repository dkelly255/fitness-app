from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('programmes/', views.all_programmes, name='programmes'),
    path('programmes/<programme_id>', views.programme_detail, name='programme_detail'),
]