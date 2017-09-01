from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^add/$', view=views.AddCustomerView.as_view(), name='add'),
    url(regex=r'^detail/(?P<pk>\w+)/$', view=views.CustomerDetailView.as_view(), name='detail'),
]
