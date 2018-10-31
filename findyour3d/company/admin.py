from django.contrib import admin
from .models import Company, SpecialOffer


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email')
    search_fields = ('name', 'user__username', 'email', 'display_name', 'phone')
    list_filter = ('is_cad_assistance', )
    ordering = ['created_at', ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(SpecialOffer)
