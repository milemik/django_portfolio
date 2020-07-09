from django import forms
from .models import ClientJobs


class JobForm(forms.Form):
    title = forms.CharField()
    image_form = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea())


class ClientJobsForm(forms.ModelForm):

    class Meta:
        model = ClientJobs
        fields = ['jobtitle', 'jobimage', 'jobdescription', 'all_see']
