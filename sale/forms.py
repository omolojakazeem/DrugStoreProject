from django import forms
from drug.models import DrugItem
from customer.models import Customer
from .models import SalesOrder


class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer','item','quantity']


    #customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    #item = forms.ModelChoiceField(queryset=DrugItem.objects.all())
    #quantity = forms.IntegerField()
