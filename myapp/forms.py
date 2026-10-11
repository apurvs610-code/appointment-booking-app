from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({'placeholder': 'Patient Name'})
            self.fields['phone'].widget.attrs.update({'placeholder': 'Phone Number'})
            self.fields['doctor'].widget.attrs.update({'placeholder': 'Doctor Name'})
            self.fields['date'].widget.attrs.update({'placeholder': 'Appointment Date yyyy-mm-dd'})
            self.fields['time'].widget.attrs.update({'placeholder': 'Appointment Time hh:mm'})
            self.fields['problem'].widget.attrs.update({'placeholder': 'What is Problem'})