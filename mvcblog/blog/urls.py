from django.conf.urls import url
from django.contrib import admin

from .views import (blog_list, blog_create, blog_detail, blog_update, blog_delete)                                                        #imports my views

urlpatterns = [
    url(r'^$', blog_list, name='list'),
    url(r'^create/$', blog_create),                                             #url for home page
    url(r'^(?P<id>\d+)/$', blog_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', blog_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', blog_delete),
]
