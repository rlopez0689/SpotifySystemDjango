from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField()

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return self.cleaned_data
        raise forms.ValidationError(("This username has already existed."))
