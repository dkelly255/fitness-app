from django.contrib import admin
from .models import Product, Category, Programme

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'description',
        'image',
    )

    ordering = ('description',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Programme, ProgrammeAdmin)