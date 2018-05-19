from django.conf.urls import url
from . import views

#routes to perform logic w/db, or render template

urlpatterns = [
    url(r'^$', views.index), #render login/reg page
    url(r'^register$', views.register), #validate, add to db, redirect to ('/')
    url(r'^login$', views.login), #validate, redirect to welcome page
    url(r'^create$', views.create), #render add book page
    url(r'^review$', views.review), #validates, adds review to db, redirects to book
    url(r'^welcome/(?P<user_id>\d+)$', views.welcome), #render welcome page, user_id passed in
    url(r'^book/(?P<book_id>\d+)/show$', views.book), #render book page passed in
    url(r'^user/(?P<user_id>\d+)/show$', views.user), #renders user page, passed in
]
