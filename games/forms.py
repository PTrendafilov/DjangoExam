from cProfile import label
from pyexpat import model
from django import forms

from games.models import *

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                    'min':12,
                }),
            'password':forms.PasswordInput(
               attrs={
                    'placeholder': 'Password',
                }),
            'first_name':forms.HiddenInput(),
            'last_name':forms.HiddenInput(),
            'picture':forms.HiddenInput(),
        }
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
class CreateGameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields = '__all__'
