from django.db import IntegrityError
from django.test import TestCase

from python_test.models import Address, Client


class TestAddress(TestCase):

    def setUp(self):
        self.client = Client.objects.create(client_name="Digital Classifieds Group", contact_name="Mathew Care",
                                            email="mathew.care@hausples.com.pg",
                                            phone_number="+61398409510")

    def test_address_with_valid_values_creates_client_object(self):
        address = Address.objects.create(street_name="some street", suburb="Mordialloc", postcode=3195, state="VIC",
                                         client=self.client)

        self.assertIsNotNone(Address.objects.get(id=address.id))
        self.assertEqual(self.client, address.client)
        self.assertEqual("some street", address.street_name)
        self.assertEqual("Mordialloc", address.suburb)
        self.assertEqual(3195, address.postcode)
        self.assertEqual("VIC", address.state)

    def test_str(self):
        address = Address.objects.create(street_name="some street 1", client=self.client,
                                         suburb="Mordialloc", postcode=3195, state="VIC")

        self.assertEqual('Street: some street 1, Suburb: Mordialloc, PostCode: 3195, State: VIC', str(address))


class TestClient(TestCase):

    def test_create_client_with_valid_values(self):
        client = Client.objects.create(client_name="Digital Classifieds Group",
                                       contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                       phone_number="+61398409510")

        self.assertIsNotNone(Client.objects.get(id=client.id))
        self.assertEqual("Digital Classifieds Group", client.client_name)
        self.assertEqual("Mathew Care", client.contact_name)
        self.assertEqual("mathew.care@hausples.com.pg", client.email)
        self.assertEqual("+61398409510", client.phone_number)

    def test_client_raises_value_error_with_a_incorrect_phone_number(self):
        with self.assertRaises(ValueError) as error:
            Client.objects.create(client_name="Digital Classifieds Group",
                                  contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                  phone_number="1212")
        self.assertIn("not a valid phone number.", str(error.exception))

    def test_client_with_a_duplicate_entry_with_same_client_name_raises_integrity_error(self):
        with self.assertRaises(IntegrityError) as error:
            Client.objects.create(client_name="Digital Classifieds Group",
                                  contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                  phone_number="+61398409510")

            Client.objects.create(client_name="Digital Classifieds Group",
                                  contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                  phone_number="+61398409510")

        self.assertIn("UNIQUE constraint failed", str(error.exception))

    def test_client_with_different_client_name_but_duplicate_email_id_entry_creates_client_object(self):
        Client.objects.create(client_name="Digital Classifieds Group",
                              contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                              phone_number="+61398409510")

        Client.objects.create(client_name="DCG",
                              contact_name="Mathew", email="mathew.care@hausples.com.pg",
                              phone_number="+61398409511")

        client = Client.objects.all()
        self.assertEqual(len(client), 2)

    def test_str(self):
        client = Client.objects.create(client_name="Digital Classifieds Group",
                                       contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                       phone_number="+61398409510")

        self.assertEqual(
            'Client Name: Digital Classifieds Group, Contact Name: Mathew Care, Email: mathew.care@hausples.com.pg, '
            'Phone Number: +61398409510',
            str(client))

    def test_address(self):
        client = Client.objects.create(client_name="Digital Classifieds Group",
                                       contact_name="Mathew Care", email="mathew.care@hausples.com.pg",
                                       phone_number="+61398409510")
        address_1 = Address.objects.create(street_name="some street 1", client=client,
                                           suburb="Mordialloc", postcode=3195, state="VIC")
        address_2 = Address.objects.create(street_name="some street 2", client=client,
                                           suburb="DDD", postcode=3195, state="VIC")

        client_addresses = client.addresses
        self.assertEqual(2, len(client_addresses))
        self.assertIn(address_1, client_addresses)
        self.assertIn(address_2, client_addresses)
