from django import forms
from .models import PricaModel


class PricaForm(forms.ModelForm):
    class Meta:
        model = PricaModel
        fields = ["text"]


class AdminPricaForm(forms.ModelForm):
    class Meta:
        model = PricaModel
        fields = (
            "reciever",
            "text",
        )
