from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy/(?P<item_id>\d+)', views.process),
    url(r'^checkout$', views.checkout),
]
