from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
