from django import forms
from .models import bookings
class DateInput(forms.DateInput):
     input_type='date'


class bookingsForm(forms.ModelForm):
    class Meta:
        model=bookings
        fields='__all__'

        widgets = {
            'booking_date':DateInput(),
        }
        labels={
            'p_name':"patient Name:",
            'p_phone':"patient phone:",
            'p_email':"patient Email:",
            'doc_name':"doctorName:",
            'booking_date':"booking Date:"}