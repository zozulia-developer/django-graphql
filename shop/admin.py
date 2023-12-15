from django.contrib import admin

from .models import Shop, Product, Category, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]


admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
