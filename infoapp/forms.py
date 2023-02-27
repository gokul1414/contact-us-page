from django import forms
from .models import ContactDatas
class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactDatas
        fields="__all__"


        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            
        }