from django import forms


class JobForm(forms.Form):
    title = forms.CharField()
    image_form = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea())
