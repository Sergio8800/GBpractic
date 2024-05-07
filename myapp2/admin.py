from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'price', 'quantity']
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category')


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
