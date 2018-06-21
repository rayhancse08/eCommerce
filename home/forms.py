from django.forms import ModelForm
from django import forms
from .models import User

class SignupForm(ModelForm):

    class Meta:
        model=User
        fields=['user_name','password','mobile_no','email']

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['user_name','password']


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)