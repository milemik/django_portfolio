from django import forms


class BlogForm(forms.Form):
    title = forms.CharField()
    blog_image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea())
