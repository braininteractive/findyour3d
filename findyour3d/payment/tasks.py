import stripe
from celery import task
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from .models import UserPayment
from findyour3d.company.models import Company


@task.periodic_task(run_every=timedelta(days=1))
def get_three_month_payments():
    three_month_payments()


def three_month_payments():
    companies = Company.objects.filter(user__payment_active=True, user__plan=2)
    for company in companies:
        if company.user.next_pay_day_on_three_month_plan():
            if timezone.now().date() >= company.user.next_pay_day_on_three_month_plan():
                charge(company.user, settings.THREE_MONTH_AMOUNT)


@task.periodic_task(run_every=timedelta(days=1))
def get_one_year_payments():
    one_year_payments()


def one_year_payments():
    companies = Company.objects.filter(user__payment_active=True, user__plan=3)
    for company in companies:
        if company.user.next_pay_day_on_one_year_plan():
            if timezone.now().date() >= company.user.next_pay_day_on_one_year_plan():
                charge(company.user, settings.ONE_YEAR_AMOUNT)


def charge(user, amount):
    payment = UserPayment.objects.create(
        user=user,
        amount=amount,
        description="Payment for Premium Plan"
    )
    charge = stripe.Charge.create(
        amount=int(amount * 100),
        currency="usd",
        customer=user.stripe_id,
        description="Payment for Premium Plan by {}".format(user.email)
    )
    payment.trx_id = charge.id
    payment.status = '2'
    payment.history = charge
    payment.save()

