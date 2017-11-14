from django.test import TestCase, Client
from django.urls import resolve
from django.core.urlresolvers import reverse
from django.utils import timezone

from findyour3d.users.models import User


class DashboardTests(TestCase):
    def setUp(self):
        self.starter_user = User.objects.create(username='test', is_active=True,
                                                email='test@test.com', user_type=2,
                                                payment_active=True, plan=1,
                                                paid_at=timezone.now())
        self.starter_user.set_password('1234567a')
        self.starter_user.save()
        self.client = Client()
        self.client.login(username='test', password='1234567a')

        outdate = timezone.now().date() - timezone.timedelta(days=40)

