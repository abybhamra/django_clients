from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    client_name = models.CharField(max_length=50, unique=True, null=False, blank=False, db_index=True)
    contact_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False, db_index=True)
    phone_number = PhoneNumberField(max_length=20, null=False, blank=False)

    def __str__(self):
        return "Client Name: %s, Contact Name: %s, Email: %s, Phone Number: %s" % (self.client_name,
                                                                                   self.contact_name,
                                                                                   self.email, self.phone_number)

    @property
    def addresses(self):
        return Address.objects.all().filter(client=self)


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    suburb = models.CharField(max_length=10, db_index=True)
    street_name = models.CharField(max_length=50)
    postcode = models.BigIntegerField()
    state = models.CharField(max_length=10)

    def __str__(self):
        return "Street: %s, Suburb: %s, PostCode: %s, State: %s" % (self.street_name,
                                                                    self.suburb, self.postcode, self.state)
