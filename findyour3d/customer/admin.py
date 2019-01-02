from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):

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


admin.site.register(Customer, CustomerAdmin)
