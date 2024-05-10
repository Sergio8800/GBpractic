from django.contrib import admin

from .models import *


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.action(description="Добавить количество: +10")
def add_quantity(modeladmin, request, queryset):
    queryset.update(quantity=10)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'price', 'quantity']
    list_display_links = ('id', 'name')
    ordering = ['name', 'category']
    search_fields = ['name']
    actions = [reset_quantity, add_quantity]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробноеописание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
