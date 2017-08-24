from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .models import Customer
from .forms import AddCustomerForm


class AddCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddCustomerForm

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        return Customer.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
