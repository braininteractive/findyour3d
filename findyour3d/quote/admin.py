from django.contrib import admin

from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'created_at')
    raw_id_fields = ('user', 'company')


admin.site.register(QuoteRequest, QuoteRequestAdmin)
