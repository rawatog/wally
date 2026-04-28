from django import forms
from .models import Post_Wallpaper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Add Bootstrap class


class CustomLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Add Bootstrap class
            field.widget.attrs['placeholder'] = field.label  # Use field label as placeholder

            # Example: customize the error message for empty fields
            field.error_messages = {
                'required': f"{field.label} is required.",
            }

class UserImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post_Wallpaper
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        super(UserImageUploadForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Add Bootstrap class if needed
        self.fields['description'].required = False