from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new), #/new routes to "new" method
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)/show$', views.show), #/654/show routes to "show" method
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.delete),
]
