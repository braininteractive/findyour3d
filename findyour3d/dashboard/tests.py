import datetime

import stripe
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, Client

from findyour3d.users.models import User
from findyour3d.company.models import Company
from findyour3d.customer.models import Customer


STRIPE_API_KEY = 'sk_test_BS2t9JImRsscT1vyWNsPYGLK'


class DashboardTests(TestCase):
    fixtures = ['users.json', 'customers.json', 'companies.json']

    def setUp(self):
        self.now = timezone.now()

        self.client = Client()
        self.client.login(username='admin', password='123')

    def test_success_login(self):
        login = self.client.login(username='admin', password='123')
        self.assertIs(login, True)

    def test_forbidden_access_to_company(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('company:add'))
        self.assertEqual(response.status_code, 403)

    def test_customer_dashboard_access(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('dashboard:company'))
        self.assertEqual(response.status_code, 200)

    def test_match_company_and_customer(self):
        """
        user.pk: 32 => "material": 0, "process": 1, INT, "need_assistance": 1,
        company.pk: 1279 => "material": "0,1,3", "top_printing_processes": "0,1", "is_cad_assistance": true,

        """
        self.client.login(username='test10', password='1234567a')
        response = self.client.get(reverse('dashboard:company'))
        # print(response.render().content)
        self.assertContains(response, 'Halo Technologies')
        self.assertNotIn('DesignPoint', response)

    def test_match_company_without_shipping_and_customer(self):
        self.client.login(username='test1', password='1234567a')
        response = self.client.get(reverse('dashboard:company'))
        self.assertContains(response, 'Forerunner')

    def test_match_metal_company_with_same_process(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('dashboard:company'))
        self.assertContains(response, 'PrintAWorld')
