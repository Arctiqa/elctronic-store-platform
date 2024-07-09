from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronic_network.models import SupplierNode


@admin.register(SupplierNode)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'supplier', 'debts', 'created_at')

    def clear_debts_to_supplier(self, request, queryset):
        updated_count = queryset.update(debts=0)
        self.message_user(request, f'Успешно очищено задолженность у {updated_count} объектов.')

    clear_debts_to_supplier.short_description = 'Очистить задолженность перед поставщиком'

    actions = [clear_debts_to_supplier]
