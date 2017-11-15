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
    def setUp(self):
        self.now = timezone.now()
        default_card = 'card_1ArI7LElSiayVU2xj6k589HC'
        stripe_id = 'cus_BDjavlKLrRcpf5'

        self.silver_user = User.objects.create(username='silver_user',
                                               user_type=2,
                                               date_joined=self.now,
                                               is_active=True,
                                               email='silver_user@test.com',
                                               payment_active=True,
                                               default_card=default_card,
                                               stripe_id=stripe_id,
                                               plan=1)
        # Individuals, Cad Assistance, $250 - 500, Stereoligtography (SLM)'), Nylon
        self.silver_company = Company.objects.create(user=self.silver_user,
                                                     name='silver_company',
                                                     display_name='silver_company',
                                                     address_line_1='1', address_line_2='2',
                                                     full_name='silver_company', email='silver_company@mail.com',
                                                     phone='1234453534', website='asddsd.com',
                                                     ideal_customer=0, is_cad_assistance=True,
                                                     budget=2, printing_options=['1', '2'], material=['6', '10', '11'],
                                                     top_printing_processes=['1', '2'],
                                                     description='silver_company')

        self.simple_user = User.objects.create(username='simple_user', user_type=1, is_active=True,
                                               email='simple_user@test.com')
        self.simple_user.set_password('1234567a')
        self.simple_user.save()
        self.customer = Customer.objects.create(user=self.simple_user, budget=2, customer_type=0, material=6,
                                                process=2, is_advanced_filled=True)

        self.client = Client()
        self.client.login(username='simple_user', password='1234567a')

    def test_success_login(self):
        login = self.client.login(username='simple_user', password='1234567a')
        self.assertIs(login, True)

    def test_forbidden_access_to_company(self):
        self.client.login(username='simple_user', password='1234567a')
        response = self.client.get(reverse('company:add'))
        self.assertEqual(response.status_code, 403)

    def test_customer_dashboard_access(self):
        self.client.login(username='simple_user', password='1234567a')
        response = self.client.get(reverse('dashboard:company'))
        self.assertEqual(response.status_code, 200)

    def test_match_company_and_customer(self):
        self.client.login(username='simple_user', password='1234567a')
        response = self.client.get(reverse('dashboard:company'))
        self.assertContains(response, 'silver_company')
