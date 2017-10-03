from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^card/$', view=views.ChangeCardView.as_view(), name='card'),
]
