from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('search/', views.search_results, name='search'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('programmes/', views.all_programmes, name='programmes'),
    path('programmes/<int:programme_id>', views.programme_detail, name='programme_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]