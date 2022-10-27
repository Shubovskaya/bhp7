from django.contrib import admin

from .models import Category
from .models import Product, Order, Contact


class ProductTabularInline(admin.TabularInline):
    model = Product


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'SITE_TITLE'
    site_url = 'SITE_URL'
    index_title = 'INDEX_TITLE'

appadmin = AppAdminSite(name='appadmin')

@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    actions = (make_published, make_unpublished)
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    inlines = (ProductTabularInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    actions = (make_published, make_unpublished)
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = ('Введите имя товара, id, артикул, цену')
    fieldsets = (
        ('Основные натройки', {
            'fields': ('title', 'article', 'price', 'category'),
            'description': 'описание'
        }),
        ('Дополнительные настройки', {
            'fields': ('is_published', 'descr', 'count', 'image')
        })
    )
    list_editable = ('category', )
    prepopulated_fields = {'descr': ('title', 'article')}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('title', 'user', 'product', 'date_created', 'is_paid')
    list_filter = ('is_paid', 'date_created')
    search_fields = ('title', 'id')
    search_help_text = ('Введите заказ')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_created')
    list_filter = ('email', 'name')
    date_hierarchy = 'date_created'


class ContactManager(ContactAdmin):
    readonly_fields = ('email', 'name', 'message', 'date_created')


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)