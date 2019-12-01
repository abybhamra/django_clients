from django import forms
from django.forms.models import inlineformset_factory

from python_test.models import Client, Address

AddressFormset = inlineformset_factory(Client, Address,
                                       fields=('street_name', 'suburb', 'postcode', 'state',),
                                       extra=1, can_delete=False, )

SEARCH_KEY_CHOICES = STATUS_CHOICES = (
    ("client_name", "Client Name"),
    ("email", "Email"),
    ("phone_number", "Phone Number"),
    ("address__suburb", "Suburb"))


class ClientSearchForm(forms.Form):
    search_key = forms.ChoiceField(choices=SEARCH_KEY_CHOICES,
                                   widget=forms.Select(attrs={'class': 'custom-select', }), )
    search_value = forms.CharField(required=False,
                                   widget=forms.TextInput(attrs={'class': "form-control",
                                                                 'placeholder': "Search Value"}), )
