from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Customer
from .forms import AddCustomerForm, AddAdvancedCustomerForm


class AddCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddCustomerForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if self.request.user.customer_set.all():
                    if self.request.user.customer_set.first().is_advanced_filled:
                        return reverse('dashboard:company')
                        # return redirect('customers:detail', self.request.user.customer_set.first().pk)
                    else:
                        return redirect('customers:advanced', self.request.user.customer_set.first().pk)
            else:
                return HttpResponseForbidden()
        return super(AddCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        if f.material is not None and f.process is not None:
            f.is_advanced_filled = True
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.object.material is not None and self.object.process is not None:
            return reverse('dashboard:company')
        else:
            return reverse('customers:advanced', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return Customer.objects.get(user=self.request.user)

    def get_initial(self):
        initial_data = super(AddCustomerView, self).get_initial()
        initial_data['user'] = self.request.user
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddAdvancedCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddAdvancedCustomerForm
    template_name = 'customer/customer_advanced_form.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 1:
                if self.request.user.customer_set.all():
                    if self.request.user.customer_set.first().is_advanced_filled:
                        return reverse('dashboard:company')
                else:
                    return redirect('customers:add')
        return super(AddAdvancedCustomerView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.is_advanced_filled = True
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customers:detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return Customer.objects.get(id=self.kwargs['pk'])

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
