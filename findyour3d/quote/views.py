from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.conf import settings
from findyour3d.company.models import Company
from findyour3d.users.email_template import send_templated_email
from .models import QuoteRequest


@login_required
def request_quote(request, pk):
    if request.method == 'POST':
        try:
            company = Company.objects.get(id=pk)
            user = request.user
            if not QuoteRequest.objects.filter(company=company, user=request.user).exists():
                quote = QuoteRequest.objects.create(user=request.user, company=company)
                send_templated_email('Request Confirmation',
                                     'email/customer_request.html', {'user': user, 'company': company,
                                                                     'quote': quote}, [user.email],
                                     'Action Needed - Job Overdue <{}{}>'.format(company.id,
                                                                                 settings.DEFAULT_FROM_EMAIL))

                return redirect('dashboard:company')
            else:
                print('already requested')
        except Company.DoesNotExist:
            print('no company found')
    else:
        print('throw an request error')
