from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    ordering = ('created_at',)

admin.site.register(Category, CategoryAdmin)
