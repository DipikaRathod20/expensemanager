from django import forms
from .models import Expense,Receipts


class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['user']
        widgets = {
            'expDateTime' : forms.DateInput(attrs={'type': 'date'})
        }

        
class ReceiptCreationForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields ='__all__'        