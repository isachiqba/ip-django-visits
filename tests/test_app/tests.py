# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import unittest
from django.core.urlresolvers import reverse

from django.test.client import RequestFactory

from visits.models import Visit
from visits.middleware import CounterMiddleware

class TestSuperView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_url_visits(self):
        request1 = self.factory.get(reverse('test-home'), REMOTE_ADDR='127.0.0.2')
        request2 = self.factory.get(reverse('test-home'), REMOTE_ADDR='127.0.0.3')

        mdl = CounterMiddleware()
        mdl.process_request(request1)
        mdl.process_request(request2)

        qs = Visit.objects.get_uri_visits_for(request2, uri=reverse('test-home'))

        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs[0].visits, 2)
