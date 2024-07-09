from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronic_network.models import SupplierNode, Contacts, Product


@admin.register(SupplierNode)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'supplier', 'debts', 'created_at', 'hierarchy_level')

    def clear_debts_to_supplier(self, request, queryset):
        updated_count = queryset.update(debts=0)
        self.message_user(request, f'Успешно очищено задолженность у {updated_count} объектов.')

    clear_debts_to_supplier.short_description = 'Очистить задолженность перед поставщиком'

    actions = [clear_debts_to_supplier]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # условие для скрытия поля для заполнения
        if obj is None:  # скрыть при создании нового объекта
            form.base_fields['hierarchy_level'].widget.attrs['style'] = 'display:none;'
            form.base_fields['hierarchy_level'].label = ''

        return form


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('node', 'email', 'country', 'city', 'street', 'house')
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
