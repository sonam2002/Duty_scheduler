from django import forms
from .models import DutySchedule

class DutyScheduleForm(forms.ModelForm):
    class Meta:
        model = DutySchedule
        fields = ['day', 'shift', 'doctor_name']