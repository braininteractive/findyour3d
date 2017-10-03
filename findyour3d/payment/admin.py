from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import UserPayment


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'status', 'description', 'created_at']


admin.site.register(UserPayment, UserPaymentAdmin)
