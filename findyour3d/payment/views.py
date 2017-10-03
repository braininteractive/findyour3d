import stripe
import logging

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.conf import settings
from django.forms.utils import ErrorList

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
        chosen_plan = self.request.GET.get('p')
        user = self.request.user
        context = super(ChangeCardView, self).get_context_data(**kwargs)
        if chosen_plan:
            context['plan'] = '1'
        else:
            context['plan'] = None

        context['user'] = user
        context['payment_active'] = user.payment_active
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangeCardView, self).dispatch(*args, **kwargs)
