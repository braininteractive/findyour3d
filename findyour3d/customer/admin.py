from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_budget_display', 'get_material',
                    'get_process', 'is_expedited')
    search_fields = ('user__username', 'user__email')

    fieldsets = [
        (None, {
            'fields': (
                'user',)
        }),
        ('Customer Profile', {'fields': ('prototype_type', 'material', 'process', 'size',
                                         'need_assistance', 'is_time_sensitive',
                                         'description', 'cad_file')}),
        ('Shipping', {'fields': ('is_expedited', 'shipping')}),
    ]

    def get_material(self, obj):
        customer = Customer.objects.get(pk=obj.id)
        return customer.get_material_display()

    def get_process(self, obj):
        customer = Customer.objects.get(pk=obj.id)
        return customer.get_process_display()

    get_material.short_description = 'material'
    get_process.short_description = 'process'


admin.site.register(Customer, CustomerAdmin)
