from django.forms.models import inlineformset_factory

from python_test.models import Client, Address

AddressFormset = inlineformset_factory(Client, Address,
                                       fields=('street_name', 'suburb', 'postcode', 'state',),
                                       extra=1, can_delete=False,)
