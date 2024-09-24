from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product administration interface for admin."""
    list_display = ('id', 'name', 'product_model', 'create_date', 'company')
    search_fields = ('name',)
