from django.contrib import admin

# Register your models here.
from .models import Product,Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','quantity','image')
    list_display_links=('name',)
    list_per_page=50
    ordering=['name']
    search_field=['name','description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description','created_at','updated_at')
    list_display_links=('name',)
    list_per_page=50
    ordering=['name']
    search_fields=['name','description']
