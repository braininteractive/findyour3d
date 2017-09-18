from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.user_type == 1:
            if self.request.user.customer_set.all():
                if self.request.user.customer_set.first().is_advanced_filled:
                    return reverse('dashboard:company')
                else:
                    return redirect('customers:advanced', self.request.user.customer_set.first().pk)
            else:
                return reverse('customers:add')

        elif self.request.user.user_type == 2:
            if self.request.user.company_set.all():
                return reverse('company:detail', kwargs={'pk': self.request.user.company_set.first().pk})
            else:
                return reverse('company:add')
        else:
            return HttpResponseForbidden()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
