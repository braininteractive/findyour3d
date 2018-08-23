from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import ListView

from findyour3d.company.models import Company


class DashboardView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'dashboard/company.html'
    context_object_name = 'companies'
    paginate_by = 50

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if not self.request.user.customer_set.all():
                    return redirect('customers:add')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user.customer_set.first()

        if user.material in [9, 12, 13, 14]:  # showing metals with SLM / DMLS
            queryset = Company.objects.filter(Q(top_printing_processes='1') &
                                              Q(budget__contains=str(user.budget)) &
                                              Q(ideal_customer__contains=str(user.customer_type)),
                                              quote_limit__gt=0).order_by(
                '-user__plan')
            if not user.need_assistance:
                queryset = queryset.filter(Q(is_cad_assistance=False) | Q(is_cad_assistance=True))
            else:
                queryset = queryset.filter(is_cad_assistance=True)
        elif user.material in [16, ]:  # material is PEEK, no need to look at process
            queryset = Company.objects.filter(Q(material__contains='16') &
                                              Q(budget__contains=str(user.budget)) &
                                              Q(ideal_customer__contains=str(user.customer_type)),
                                              quote_limit__gt=0).order_by(
                '-user__plan')
            if not user.need_assistance:
                queryset = queryset.filter(Q(is_cad_assistance=False) | Q(is_cad_assistance=True))
            else:
                queryset = queryset.filter(is_cad_assistance=True)
        else:
            queryset = Company.objects.filter(
                (Q(material__contains=str(user.material))) &
                Q(top_printing_processes__contains=str(user.process)) &
                Q(budget__contains=str(user.budget)) &
                Q(ideal_customer__contains=str(user.customer_type)), quote_limit__gt=0).order_by('-user__plan')
            if not user.need_assistance:
                queryset = queryset.filter(Q(is_cad_assistance=False) | Q(is_cad_assistance=True))
            else:
                queryset = queryset.filter(is_cad_assistance=True)
        return queryset


