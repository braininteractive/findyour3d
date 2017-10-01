from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Company
from .forms import AddCompanyForm


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
        return reverse('company:detail', kwargs={'pk': self.object.id})

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
    template_name = 'company/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['company_pk'] = self.object
        return context


class EditCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = AddCompanyForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            if self.request.user.user_type == 2:
                if not self.request.user.company_set.all():
                    return redirect('company:add')
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
