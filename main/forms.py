# forms.py
from datetime import time
from django import forms
from .models import Order, TIME_CHOICES



# forms.py
from django import forms
from .models import Order
from django.utils import timezone

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['scheduled_date', 'scheduled_time', ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['scheduled_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        self.fields['scheduled_time'].widget = forms.Select(choices=TIME_CHOICES, attrs={'class': 'form-control'})
        #self.fields['scheduled_time'].widget = forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})


