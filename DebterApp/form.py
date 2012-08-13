# -*- coding: UTF-8 -*-

from django import forms
from models import *

class NewDebtForm(forms.Form):
    user = forms.ChoiceField(choices=[ (user.first_name, user.last_name) for user in User.objects.all()])
    title = forms.CharField( max_length=10, required=True )
    amount = forms.DecimalField( max_digits=5, decimal_places=2, required=True )
    description = forms.CharField( widget=forms.Textarea(), required=False, max_length=1000 )
    date_of_loan = forms.DateField( required=True, input_formats='%Y-%m-%d' )
    date_of_repayment = forms.DateField( required=True, input_formats='%Y-%m-%d' )

