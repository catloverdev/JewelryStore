from django import forms
from jewelry_store.models import Client


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

