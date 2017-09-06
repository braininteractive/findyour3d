from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ('email', 'is_sent', )

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_sent:
            return self.readonly_fields + ('is_sent', 'reply_text')
        elif obj:
            return self.readonly_fields + ('is_sent', )
        return self.readonly_fields

admin.site.register(Contact, ContactAdmin)
