from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^request/(?P<pk>\w+)/$', view=views.request_quote, name='req'),
]
