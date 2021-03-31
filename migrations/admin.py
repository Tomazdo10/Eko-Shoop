from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "description",
        "price",
        "rating",
        "image",
        "image_url",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',

    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)