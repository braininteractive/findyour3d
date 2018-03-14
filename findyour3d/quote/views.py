import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from findyour3d.payment.views import starter_charge
from findyour3d.users.email_template import send_templated_email
from findyour3d.utils.views import custom_redirect

from findyour3d.company.models import Company
from .models import QuoteRequest


logger = logging.getLogger(__name__)


@login_required
def request_quote(request, pk):
    if request.method == 'POST':
        try:
            company = Company.objects.get(id=pk)
            company_owner = company.user
            company_plan = company_owner.plan
            user = request.user
            if company_plan is not None:
                if not QuoteRequest.objects.filter(company=company, user=request.user).exists():
                    quote = QuoteRequest.objects.create(user=request.user, company=company)

                    # sending email to company
                    send_templated_email('Your3d: New Request Received',
                                         'email/customer_request.html',
                                         {'user': user, 'company': company, 'quote': quote},
                                         [company.email])

                    # sending email to customer
                    send_templated_email('Your3d: Request Confirmation',
                                         'email/company_request.html',
                                         {'user': user, 'company': company, 'quote': quote},
                                         [user.email])

                    if company_plan == 1:
                        starter_charge(company_owner)
                        company.quote_limit -= 1
                        company.save()
                        return custom_redirect('dashboard:company', quote='requested')
                    else:
                        return custom_redirect('dashboard:company', quote='requested')
                else:
                    logger.error('already requested')
                    return redirect('dashboard:company')
            else:
                logger.error('company without plan')
                return redirect('dashboard:company')
        except Company.DoesNotExist:
            logger.error('no company found')
            return redirect('dashboard:company')
    else:
        logger.error('throw an request error')
        return redirect('dashboard:company')
