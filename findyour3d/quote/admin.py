from django.contrib import admin

from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'created_at')


admin.site.register(QuoteRequest, QuoteRequestAdmin)
