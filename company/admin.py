from django.contrib import admin

from company.models import Supplier, Company


def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


clear_debt.short_description = "Очистить задолженность"

fields_display = [
    'supplier_name',
    'debt',
    'customer',
    'supplier',
    'owner',
]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin interface for supplier."""
    list_display = fields_display
    actions = [clear_debt]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Company administration interface for admin."""
    list_display = ('id', 'name', 'email', 'country', 'city', 'company_type', 'number_bld', 'street',
                    'owner')
    list_filter = ('city',)
    search_fields = ('city',)
