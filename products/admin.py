from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category', 'image')
    readonly_fields = ('name', 'description')
    ordering = ('name',)
    search_fields = ('name',)
