from django.contrib import admin

from electronic_network.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNode(admin.ModelAdmin):
    list_display = ('name', 'type', 'email', 'country', 'city', 'supplier', 'debts', 'created_at')
    list_filter = ('city',)

    def clear_debts_to_supplier(self, request, queryset):
        updated_count = queryset.update(debts=0)
        self.message_user(request, f'Успешно очищено задолженность у {updated_count} объектов.')

    clear_debts_to_supplier.short_description = 'Очистить задолженность перед поставщиком'

    actions = [clear_debts_to_supplier]
