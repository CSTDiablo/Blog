from django import forms
from .models import (ContactUs,)

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs= {'class':'form-control','placeholder':'Your Name','id':'name'}),
            'email' : forms.EmailInput(attrs= {'class':'form-control','placeholder':'email','id':'email'}),
            'subject' : forms.TextInput(attrs= {'class':'form-control','placeholder':'subject','id':'subject'}),
            'message' : forms.Textarea(attrs= {'class':'form-control','placeholder':'message','rows':5}),

            

        }

