from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .models import Customer
from .forms import AddCustomerForm, AddAdvancedCustomerForm


class AddCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddCustomerForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_type == 1:
            if self.request.user.customer_set.all():
                if self.request.user.customer_set.first().is_advanced_filled:
                    return redirect('customers:detail', self.request.user.customer_set.first().pk)
                else:
                    return redirect('customers:advanced')
        else:
            return HttpResponseForbidden()
        return super(AddCustomerView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('customers:advanced')

    def get_object(self):
        return Customer.objects.get(user=self.request.user)

    def get_initial(self):
        initial_data = super(AddCustomerView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddAdvancedCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddAdvancedCustomerForm
    template_name = 'customer/customer_advanced_form.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_type == 1:
            if self.request.user.customer_set.all():
                if self.request.user.customer_set.first().is_advanced_filled:
                    return redirect('customers:detail', self.request.user.customer_set.first().pk)
        return super(AddAdvancedCustomerView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('customers:detail', kwargs={'pk': self.object.id})

    def get_object(self):
        return Customer.objects.get(user=self.request.user)

    def get_initial(self):
        initial_data = super(AddAdvancedCustomerView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['customer_pk'] = self.object
        return context
