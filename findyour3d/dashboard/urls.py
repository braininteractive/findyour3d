from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^company/$', view=views.company, name='company'),
]
