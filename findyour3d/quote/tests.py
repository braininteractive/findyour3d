from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils import timezone

from findyour3d.company.models import Company
from findyour3d.customer.models import Customer
from findyour3d.quote.models import QuoteRequest
from findyour3d.users.models import User


class DashboardTests(TestCase):
    def setUp(self):
        self.now = timezone.now()
        default_card = 'card_1ArI7LElSiayVU2xj6k589HC'
        stripe_id = 'cus_BDjavlKLrRcpf5'
        self.starter_user = User.objects.create(username='test', is_active=True,
                                                email='test@test.com', user_type=2,
                                                payment_active=True, plan=1,
                                                paid_at=timezone.now())
        self.customer = Customer.objects.create(user=self.starter_user,
                                                budget=2,
                                                customer_type=0,
                                                material='6',
                                                process='2',
                                                is_advanced_filled=True,
                                                shipping='1',
                                                need_assistance=1)

        self.starter_user.set_password('1234567a')
        self.starter_user.save()
        self.client = Client()
        self.client.login(username='test', password='1234567a')

        self.metal_company_user = User.objects.create(username='metal_user',
                                                      user_type=2,
                                                      date_joined=self.now,
                                                      is_active=True,
                                                      email='metal_user@test.com',
                                                      payment_active=True,
                                                      default_card=default_card,
                                                      stripe_id=stripe_id,
                                                      plan=1)

        # Individuals, Cad Assistance, $250 - 500, Stereoligtography (SLM)'), Copper
        self.metal_company = Company.objects.create(user=self.metal_company_user,
                                                    name='metal_company',
                                                    display_name='metal_company',
                                                    address_line_1='1', address_line_2='2',
                                                    full_name='metal_company', email='metal_company@mail.com',
                                                    phone='1234453534', website='metal_company.com',
                                                    ideal_customer=['0', ],
                                                    is_cad_assistance=True,
                                                    budget=['2', ],
                                                    printing_options=['1', ],
                                                    material=['13', ],
                                                    top_printing_processes=['1', ],
                                                    description='metal_company',
                                                    shipping=['0', '1', '2'])

    def test_request_quote(self):
        response = self.client.post(reverse('quote:req', kwargs={'pk': self.metal_company.pk}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(QuoteRequest.objects.count(), 1)


