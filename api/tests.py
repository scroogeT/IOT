# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import device

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.device_make = "chakonyonyo"
        self.device = device(make = self.device_make)

        def test_model_can_create_a_device(self):
            old_count = device.objects.count()
            self.device.save()
            new_count = device.objects.count()
            self.assertNotEqual(old_count,new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.device_data = {'owner':'Gogo','make':'homeDev'}
        self.response = self.client.post(
            reverse('create'),
            self.device_data,
            format="json"
        )

    def test_api_can_create_a_device(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

