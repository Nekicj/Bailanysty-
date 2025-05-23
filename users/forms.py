from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(max_length=500, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'bio', 'location', 'website', 'profile_picture')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your full name'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tell us about yourself'})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your location'})
        self.fields['website'].widget.attrs.update({'class': 'form-control', 'placeholder': 'https://example.com'})
