from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import ListView

from findyour3d.company.models import Company


class DashboardView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'dashboard/company.html'
    context_object_name = 'companies'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if not self.request.user.customer_set.all():
                    return redirect('customers:add')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user.customer_set.first()
        queryset = Company.objects.filter(
            (Q(material=user.material) & Q(top_printing_processes__contains=str(user.process)))
            & Q(budget=user.budget)
        )
        return queryset

