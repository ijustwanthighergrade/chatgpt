from django import forms
#from .models import Participates
from .models import participate

class ParticipateForm(forms.ModelForm):
    class Meta:
        model = participate
        fields = ['Name', 'MID', 'birthday', 'insurance_status']
        labels = {
            #'booking_number': '訂單編號',
            'Name': '參加人姓名',
            'MID': '身分證字號',
            'birthday': '出生年月日',
            'insurance_status': '保險狀態'
        }
        widgets = {
            #'booking_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'MID': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'insurance_status': forms.Select(attrs={'class': 'form-control'}),
        }
