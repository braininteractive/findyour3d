import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings

from findyour3d.payment.models import Coupon
from findyour3d.utils.views import get_amount_with_discount
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


@login_required
def user_plan(request):
    user = request.user
    three_amount_amount = get_amount_with_discount(user, settings.THREE_MONTH_AMOUNT)
    one_year_amount = get_amount_with_discount(user, settings.ONE_YEAR_AMOUNT)
    has_coupon = False
    if Coupon.objects.filter(activated_by=user).exists():
        has_coupon = True
    data = {
        'three_amount_amount': three_amount_amount,
        'one_year_amount': one_year_amount,
        'has_coupon': has_coupon
    }
    if user.user_type == 2:
        return render(request, 'company/company_plan.html', data)
    return redirect('users:redirect')


@login_required
def cancel(request):
    if request.method == 'POST':
        user = request.user
        if user.user_type == 2:
            user.is_cancelled = True
            user.plan = None
            user.save()
            return HttpResponse(json.dumps({"status": True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status": False}), content_type="application/json")
