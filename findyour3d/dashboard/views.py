from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from findyour3d.company.models import Company


@login_required
def company(request):
    user = request.user.customer_set.first()
    companies = Company.objects.filter(
        Q(material=user.material) | Q(top_printing_processes=str(user.process)) | Q(printing_options=str(user.process))
    )
    data = {
        'companies': companies
    }
    return render(request, 'dashboard/company.html', data)
