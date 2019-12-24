from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False) 

    class Meta:
        model = User
        fields = ( 'username','email', 'password1', 'password2', 'image')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.image = self.cleaned_data.get('image')
        user.save()
        user.userprofile.image = self.cleaned_data.get('image')
        user.userprofile.save()
        if commit:
        	user.save()
        return user