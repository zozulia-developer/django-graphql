from django.contrib import admin

from .forms import ProductAdminForm
from .models import Shop, Product, Category, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'admin/shop/product_change_form.html'
    form = ProductAdminForm
    inlines = [ProductImageAdmin]


admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
