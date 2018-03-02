from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import UserPayment, Coupon


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'status', 'description', 'created_at']


class CouponAdmin(admin.ModelAdmin):
    list_display = ('number', 'discount', 'expired')
    raw_id_fields = ('activated_by', )


admin.site.register(UserPayment, UserPaymentAdmin)
admin.site.register(Coupon, CouponAdmin)
