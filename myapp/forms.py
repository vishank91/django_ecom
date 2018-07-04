from .models import Product,Checkout,Cart
from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
class Product_form(forms.ModelForm):
    class Meta():
        model=Product
        fields='__all__'

class Checkout_form(forms.ModelForm):
    class Meta():
        model=Checkout
        fields='__all__'


class Cart_form(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['quantity']


class User_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
                'placeholder':'Enter User Name'}
    ),required=True,max_length=20)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Mail Id'}
    ), required=True, max_length=20)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter First Name'}
    ),required=True,max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Lasr Name'}
    ),required=True,max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=20)
    confirm_password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=20)

    class Meta():
        model=User
        fields=['username','email','first_name','last_name','password']

    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match=User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("User Name Already Exist")

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            ma=validate_email(email)
        except:
            raise forms.ValidationError("Email is not Valid")
        return email

    def clean_confirm_password(self):
        p=self.cleaned_data['password']
        cp=self.cleaned_data['confirm_password']

        if(p!=cp):
            raise forms.ValidationError("Confirm Password and Password Must be Same")
        else:
            if(len(p)<8):
                raise forms.ValidationError("Password must be atleast 8 Character")
            if(p.isdigit()):
                raise forms.ValidationError("Password must contains aleast a character")
