from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse

from python_test.forms import AddressFormset
from python_test.models import Client


class ClientCreateViewTests(SimpleTestCase):

    def test_view_url_by_name(self):
        response = self.client.get(reverse('client-create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/new.html')
        self.assertIsInstance(response.context["address"], AddressFormset)


class ClientListViewTests(TestCase):

    def setUp(self):
        Client.objects.create(client_name="Digital Classifieds Group",
                              email="mathew.care@hausples.com.pg",
                              phone_number="+61398409510")

    def test_clients_view_lists_clients(self):
        response = self.client.get(reverse('client-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/list.html')
