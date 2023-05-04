from django import forms


class AddList(forms.Form):
    name = forms.CharField(label="name", max_length=255)
