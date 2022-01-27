from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ('user', 'email_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Name',
            'surname': 'Surname',
            'email': 'email@example.com',
            'order_number': "You'll find this in your confirmation email ",
            'query': "Any comments or questions you may have",
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
