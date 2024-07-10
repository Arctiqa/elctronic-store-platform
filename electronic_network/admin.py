from django.contrib import admin
from django.utils.html import format_html

from electronic_network.models import SupplierNode, Contacts, Product


@admin.register(SupplierNode)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'get_supplier', 'debts', 'created_at', 'hierarchy_level', 'get_products')

    def clear_debts_to_supplier(self, request, queryset):
        """Функция для очистки задолженности перед поставщиком в административной панели"""

        updated_count = queryset.update(debts=0)
        self.message_user(request, f'Успешно очищено задолженность у {updated_count} объектов.')

    clear_debts_to_supplier.short_description = 'Очистить задолженность перед поставщиком'

    actions = [clear_debts_to_supplier]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj is None:
            form.base_fields['hierarchy_level'].widget.attrs['style'] = 'display:none;'
            form.base_fields['hierarchy_level'].label = ''

        return form

    @admin.display(description="Товары")
    def get_products(self, instance):
        products = instance.products.all()
        return ', '.join([product.name for product in products])

    @admin.display(description="Поставщик")
    def get_supplier(self, obj):
        if obj.supplier:
            return format_html("<a href='{}'>{}</a>", obj.supplier.id, obj.supplier.name)
        return "-"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'email', 'country', 'city', 'street', 'house')
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
