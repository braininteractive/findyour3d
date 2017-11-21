from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.AddCompanyView.as_view(), name='add'),
    url(regex=r'^detail/(?P<pk>\w+)/$', view=views.CompanyDetailView.as_view(), name='detail'),
    url(regex=r'^edit/(?P<pk>\w+)/$', view=views.EditCompanyView.as_view(), name='edit'),

    url(r'^offer/add/$', views.AddSpecialOfferView.as_view(), name='add_offer'),
]
