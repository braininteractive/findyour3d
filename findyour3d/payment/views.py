import stripe
import logging

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.conf import settings
from django.forms.utils import ErrorList

from .models import UserPayment
from .forms import CreditCardForm

stripe.api_key = settings.STRIPE_API_KEY
logger = logging.getLogger(__name__)


class ChangeCardView(FormView):
    template_name = 'payment/card.html'
    success_url = '/'
    form_class = CreditCardForm

    def form_valid(self, form):
        try:
            token = stripe.Token.create(card={
                "number": form.cleaned_data['number'],
                "exp_month": form.cleaned_data["expiration"].month,
                "exp_year": form.cleaned_data["expiration"].year,
                "cvc": form.cleaned_data['cvc'],
                'name': form.cleaned_data['name'],
            },)

            customer = stripe.Customer.create(source=token.id,
                                              description="Payment for {}".format(
                                                  self.request.user.username), )

            user = self.request.user
            user.stripe_id = customer['id']
            user.default_card = customer['default_source']
            card = customer['sources']['data'][0]
            user.card_type = card['brand']
            user.card_last = card['last4']
            user.card_expiry = '{}/{}'.format(str(card['exp_month']), str(card['exp_year']))
            user.payment_active = True
            user.save()

            return super(ChangeCardView, self).form_valid(form)
        except Exception as e:
            logger.exception('Exception on Credit Card add/edit: {}'.format(e))
            errors = form._errors.setdefault("number", ErrorList())
            errors.append(e.message)
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        plan = self.request.GET.get('plan')
        user = self.request.user
        context = super(ChangeCardView, self).get_context_data(**kwargs)
        context['payment_active'] = user.payment_active
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangeCardView, self).dispatch(*args, **kwargs)


class StartPlan(ChangeCardView):
    """
    Adding Card to user and redirects user to specified plan_id with GET parameter `plan`
    /make/?plan=1 will be processed with make_payment function
    """
    def get_success_url(self):
        url = "{}?plan={}".format(reverse_lazy('payments:make'), self.request.GET.get('plan'))
        return url


@login_required
def make_payment(request):

    three_month_amount = 105.00
    one_year_amount = 360.00

    user = request.user

    if request.GET.get('plan'):
        plan_id = request.GET.get('plan')

        try:
            plan_id = int(plan_id)
        except ValueError:
            plan_id = None

        if plan_id:
            try:
                amount = 0
                if plan_id == 2:  # premium
                    amount = three_month_amount
                elif plan_id == 3:
                    amount = one_year_amount

                elif plan_id == 1:  # starter
                    user.plan = 1
                    user.save()
                    user.is_cancelled = False
                    UserPayment.objects.create(
                        user=user,
                        amount=amount,
                        status='2',
                        description="Enroll to Starter Plan by {}".format(user.email)
                    )
                    response = redirect('company:detail', user.company_set.first().pk)
                    response['Location'] += '?plan=enroll'
                    return response
                else:
                    logger.debug('wtf with plan_id')
                    return redirect('company:detail', user.company_set.first().pk)

                if amount > 0:
                    payment = UserPayment.objects.create(
                        user=user,
                        amount=amount,
                        description="Charge for Premium Plan by {}".format(user.email)
                    )
                    charge = stripe.Charge.create(
                        amount=int(amount * 100),
                        currency="usd",
                        customer=user.stripe_id,
                        description="Charge for Premium Plan by {}".format(user.email)
                    )
                    payment.trx_id = charge.id
                    payment.status = '2'
                    payment.history = charge
                    payment.save()

                    user.plan = plan_id
                    user.paid_at = timezone.now()
                    user.is_cancelled = False
                    user.save()

                    response = redirect('company:detail', request.user.company_set.first().pk)
                    response['Location'] += '?plan=enroll'
                    return response

            except Exception as e:
                logger.exception('Exception on StartPlan (add card & pay): {}'.format(e))
    return redirect('company:detail', request.user.company_set.first().pk)


def starter_charge(user):
    amount = settings.STARTER_FEE
    payment = UserPayment.objects.create(
        user=user,
        amount=amount,
        description="Quote Request"
    )
    charge = stripe.Charge.create(
        amount=int(amount * 100),
        currency="usd",
        customer=user.stripe_id,
        description="Quote Request by {}".format(user.email)
    )
    payment.trx_id = charge.id
    payment.status = '2'
    payment.history = charge
    payment.save()
