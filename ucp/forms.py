from django import forms


class NewWorkerForm(forms.Form):
    ip_addr = forms.GenericIPAddressField(label="IP Address", max_length=100, help_text="Public IP Address of the worker.")
