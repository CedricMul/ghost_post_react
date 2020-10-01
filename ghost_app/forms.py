from django import forms

class PostForm(forms.Form):
    is_boast = forms.BooleanField(required=False)
    content = forms.CharField(max_length=240)
