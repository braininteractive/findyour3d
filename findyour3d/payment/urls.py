from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^card/$', view=views.ChangeCardView.as_view(), name='card'),
    url(regex=r'^start/$', view=views.StartPlan.as_view(), name='start'),
    url(regex=r'^make/$', view=views.make_payment, name='make'),
    url(regex=r'^coupon/$', view=views.activate_coupon, name='activate_coupon'),
]
