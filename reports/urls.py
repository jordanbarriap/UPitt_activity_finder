from django.conf.urls import include, url
from . import views

from django.contrib import admin

urlpatterns = [
    url(r'^$', views.reports),
    url(r'^get_filters$', views.get_filters),
    url(r'^get_subfilters$', views.get_subfilters),
    url(r'^get_table$', views.get_table),
    url(r'^get_subtable$', views.get_subtable),
]
