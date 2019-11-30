from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from python_test.forms import AddressFormset
from python_test.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client/list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/index.html'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/new.html'
    fields = ["client_name", "contact_name", "email", "phone_number"]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["address"] = AddressFormset(self.request.POST)
        else:
            data["address"] = AddressFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context["address"]
        self.object = form.save()
        if address.is_valid():
            address.instance = self.object
            address.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("client-list")


class ClientEditView(UpdateView):
    model = Client
    template_name = 'client/edit.html'
    fields = ["client_name", "contact_name", "email", "phone_number"]

    def get_success_url(self):
        return reverse("client-list")
