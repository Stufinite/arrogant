# -*- coding: utf-8 -*-
from django.conf.urls import url
from arrogant import views

urlpatterns = [
  url(r'^get/jvalue$', views.jvalue, name='jvalue'),
  url(r'^get/jlist$', views.jlist, name='jlist'),
  url(r'^get/comment$', views.comment, name='comment'),
]