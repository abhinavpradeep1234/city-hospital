from django import forms
from .models import registration

class registrationform(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'

    


        labels  = {
            'c_name': "Client Name:",
            'c_phone': "Client Phone Number:",
            'c_email': "Client Email Id:",
            'c_qualif': "Client Qualification:",
            'company_name': "Company Name :",
        }
