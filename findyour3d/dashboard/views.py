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

    def filter_assistance(self, qs):
        user = self.request.user.customer_set.first()
        if not user.need_assistance:
            queryset = qs.filter(Q(is_cad_assistance=False) | Q(is_cad_assistance=True))
        elif not user.need_assistance and user.cad_file is not None:
            queryset = qs.filter(Q(is_cad_assistance=False) | Q(is_cad_assistance=True))
        else:
            queryset = qs.filter(is_cad_assistance=True)
        return queryset

    def filter_shipping(self, qs):
        user = self.request.user.customer_set.first()
        queryset = qs

        if user.is_expedited:
            queryset = qs.filter(is_expedited=True)

        # if user.shipping:
        #     queryset = qs.filter(Q(shipping=str(user.shipping)) | Q(shipping=[]) | Q(shipping__isnull=True))
        #     queryset = qs.filter(shipping=user.shipping)

        return queryset

    def filter_metals(self, qs):
        user = self.request.user.customer_set.first()
        queryset = qs
        if user.material in [9, 12, 13, 14]:  # showing metals with SLM / DMLS
            queryset = qs.filter(Q(top_printing_processes__contains='1') &
                                 Q(budget__contains=str(user.budget)) &
                                 Q(ideal_customer__contains=str(user.customer_type)))
        return queryset

    def filter_budget(self, qs):
        user = self.request.user.customer_set.first()
        return qs.filter(budget__contains=str(user.budget))

    def filter_customer(self, qs):
        user = self.request.user.customer_set.first()
        return qs.filter(ideal_customer__contains=str(user.customer_type))

    def get_queryset(self):
        user = self.request.user.customer_set.first()

        if user.material in [16, ]:  # material is PEEK, no need to look at process
            queryset = Company.objects.active().filter(Q(material__contains='16') &
                                                       Q(budget__contains=str(user.budget)) &
                                                       Q(ideal_customer__contains=str(user.customer_type)))
        else:
            regex_material = "(^|,)%s(,|$)" % "|".join([str(user.material), ])
            regex_process = "(^|,)%s(,|$)" % "|".join([str(user.process), ])
            queryset = Company.objects.active().filter((Q(material__regex=regex_material)) & Q(
                top_printing_processes__regex=regex_process))
            # queryset = Company.objects.active().filter(
            #     (Q(material__contains=str(user.material))) &
            #     Q(top_printing_processes__contains=str(user.process)))

        queryset = self.filter_assistance(queryset)
        queryset = self.filter_shipping(queryset)
        queryset = self.filter_metals(queryset)
        queryset = self.filter_budget(queryset)
        queryset = self.filter_customer(queryset)
        return queryset

