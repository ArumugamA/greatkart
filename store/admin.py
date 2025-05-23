from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'updated_at', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-updated_at',)

admin.site.register(Product, ProductAdmin)
