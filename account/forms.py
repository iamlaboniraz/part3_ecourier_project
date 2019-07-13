from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,driver_Profile

         ## customer profile ##
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    #############       Driver profile           #####################
class DriverRegisterForm(UserCreationForm):
    email = forms.EmailField()
    car_details = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username', 'email','car_details','phone', 'password1', 'password2']

class DriverUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class DriverProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = driver_Profile
        fields = ['image','status']
