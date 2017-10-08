import stripe
from celery import task
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from .models import UserPayment
from findyour3d.company.models import Company


@task.periodic_task(run_every=timedelta(days=1))
def get_monthly_payments():
    monthly_payments()


def monthly_payments():
    companies = Company.objects.filter(user__payment_active=True, user__plan=2)
    for company in companies:
        if company.user.next_pay_day():
            if timezone.now().date() >= company.user.next_pay_day():
                charge(company.user)


def charge(user):
    amount = settings.PREMIUM_FEE
    payment = UserPayment.objects.create(
        user=user,
        amount=amount,
        description="Monthly Payment for Premium Plan"
    )
    charge = stripe.Charge.create(
        amount=int(amount * 100),
        currency="usd",
        customer=user.stripe_id,
        description="Monthly Payment for Premium Plan by {}".format(user.email)
    )
    payment.trx_id = charge.id
    payment.status = '2'
    payment.history = charge
    payment.save()

