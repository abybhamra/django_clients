from django.test import TestCase

from python_test.forms import AddressFormset


class TestAddressFormSet(TestCase):
    def test_formset_initialisation(self):
        formset = AddressFormset()

        self.assertEqual(1, len(formset.forms))
        self.assertEqual(4, len(formset.forms[0].visible_fields()))
        labels = [field.label for field in formset.forms[0].visible_fields()]
        self.assertEqual(['Street name', 'Suburb', 'Postcode', 'State'], labels)
