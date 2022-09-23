from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = ('Введите имя товара, id, артикул, цену')


# admin.site.register(Category, CategoryAdmin)