from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .models import Company, SpecialOffer
from .forms import AddCompanyForm, EditCompanyForm, AddSpecialOfferForm

from findyour3d.payment.models import UserPayment


class AddCompanyView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = AddCompanyForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_type == 2:
            if self.request.user.company_set.all():
                return redirect('company:detail', self.request.user.company_set.first().pk)
        else:
            return HttpResponseForbidden()
        return super(AddCompanyView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:plan')
        # return reverse('company:detail', kwargs={'pk': self.object.id})

    def get_object(self):
        return Company.objects.get(user=self.request.user)

    def get_initial(self):
        initial_data = super(AddCompanyView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = super(AddCompanyView, self).get_form_kwargs()
        kwargs.update(
            {'initial':
                 {'user': self.request.user}
             }
        )
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company

    def get_template_names(self):
        company_id = self.kwargs.get('pk')
        try:
            company = Company.objects.get(pk=company_id)
            if company.user.plan == 2:
                template_name = 'company/company_detail_premium.html'
            else:
                template_name = 'company/company_detail.html'
        except Company.DoesNotExist:
            template_name = 'company/company_detail.html'

        return template_name

    def dispatch(self, request, *args, **kwargs):
        return super(CompanyDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['company_pk'] = self.object
        context['user'] = user
        context['is_owner'] = False
        if user.user_type == 2:
            if self.object.id == user.company_set.first().pk:
                context['is_owner'] = True
        member_since = None
        if UserPayment.objects.filter(user=user).exists():
            member_since = UserPayment.objects.filter(user=user).latest('created_at').created_at

        context['member_since'] = member_since
        return context


class EditCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = EditCompanyForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 2:
                if request.user.plan == 2:  # Allow only premium users
                    if int(self.kwargs['pk']) == request.user.company_set.first().pk:
                        if not self.request.user.company_set.all():
                            return redirect('company:add')
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
        return super(EditCompanyView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('company:detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return Company.objects.get(id=self.kwargs['pk'])

    def get_initial(self):
        initial_data = super(EditCompanyView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class AddSpecialOfferView(LoginRequiredMixin, CreateView):
    model = SpecialOffer
    form_class = AddSpecialOfferForm

    def get_success_url(self):
        return reverse('company:detail', kwargs={'pk': self.object.company.id})

    def get_object(self):
        return SpecialOffer.objects.get(company__user=self.request.user)

    def get_initial(self):
        initial_data = super(AddSpecialOfferView, self).get_initial()
        initial_data['company'] = Company.objects.get(user=self.request.user)
        return initial_data

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = super(AddSpecialOfferView, self).get_form_kwargs()
        kwargs.update(
            {'initial':
                 {'company': Company.objects.get(user=self.request.user)}
             }
        )
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteSpecialOfferView(LoginRequiredMixin, DeleteView):
    model = SpecialOffer

    def get_success_url(self):
        return reverse('company:detail', kwargs={'pk': self.object.company.id})
