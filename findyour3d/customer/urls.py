from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^add/$', view=views.AddCustomerView.as_view(), name='add'),
    url(regex=r'^advanced/(?P<pk>\w+)/$', view=views.AddAdvancedCustomerView.as_view(), name='advanced'),
    url(regex=r'^detail/(?P<pk>\w+)/$', view=views.CustomerDetailView.as_view(), name='detail'),
    url(regex=r'^edit/(?P<pk>\w+)/$', view=views.EditCustomerView.as_view(), name='edit'),
]
