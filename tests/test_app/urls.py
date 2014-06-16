# -*- coding: utf-8 -*-

try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url


from test_app.views import TestView1, TestView2

urlpatterns = patterns(
    '',
    url(r'^test1/$', TestView1.as_view(), name='test-home'),
    url(r'^test2/$', TestView2.as_view(), name='test-home2'),
)
