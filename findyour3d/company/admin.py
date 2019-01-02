from django.contrib import admin
from .models import Company, SpecialOffer


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'get_budget_display', 'get_material_display',
                    'get_top_printing_processes_display', 'is_expedited')
    search_fields = ('name', 'user__username', 'email', 'display_name', 'phone')
    list_filter = ('is_cad_assistance', )
    ordering = ['created_at', ]

    fieldsets = [
        (None, {
            'fields': (
                'user', 'name', 'display_name', 'logo', 'address_line_1', 'address_line_2')
        }),
        ('User Profile', {'fields': ('full_name', 'email', 'phone', 'website')}),
        ('Company Profile', {'fields': ('ideal_customer', 'is_cad_assistance', 'budget',
                                        'consideration', 'material', 'top_printing_processes',
                                        'description')}),
        ('Shipping', {'fields': ('is_expedited', 'shipping')}),
        ('Settings', {'fields': ('quote_limit', )}),
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(SpecialOffer)
