from django.db import models
from django.conf import settings


class QuoteRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey('company.Company')
    created_at = models.DateTimeField(auto_now_add=True)
