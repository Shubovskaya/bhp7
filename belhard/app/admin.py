from django.contrib import admin

# Register your models here.
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'


# admin.site.register(Category, CategoryAdmin)