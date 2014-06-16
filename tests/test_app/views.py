# -*- coding: utf-8 -*-

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext


class TestView1(View):
    template_path = 'test_page.html'

    def get(self, request):
        return render_to_response(
            self.template_path,
            {},
            context_instance=RequestContext(request)
            )


class TestView2(View):
    template_path = 'test_page2.html'

    def get(self, request):
        return render_to_response(
            self.template_path, {},
            context_instance=RequestContext(request))
