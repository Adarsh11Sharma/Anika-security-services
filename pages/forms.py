from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'surname', 'email', 'message', 'agree']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jane', 'required': True}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jane.doe@example.com', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message', 'style': 'height: 150px', 'required': True}),
            'agree': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }
