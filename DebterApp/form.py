# -*- coding: UTF-8 -*-

from django import forms
from models import *
from registration.forms import RegistrationFormUniqueEmail

class DebterRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(label='Imię',
                                 min_length=3,
                                 max_length=16,
                                 error_messages={'required': 'To pole jest wymagane.',
                                                 'min_length': 'To pole musi być dłuższe niż 3 znaki.',
                                                 'max_length': 'To pole nie może być dłuższe niż 16 znaków.'})
    last_name = forms.CharField(label='Nazwisko',
                                min_length=3,
                                max_length=16,
                                error_messages={'required': 'To pole jest wymagane.',
                                                'min_length': 'To pole musi być dłuższe niż 3 znaki.',
                                                'max_length': 'To pole nie może być dłuższe niż 16 znaków.'})

class NewDebtForm(forms.Form):
    user = forms.ChoiceField(choices=[ (user.first_name, user.last_name) for user in User.objects.all()])
    title = forms.CharField( max_length=10 )
    amount = forms.DecimalField( max_digits=5, decimal_places=2 )
    description = forms.CharField( widget=forms.Textarea(), required=False, max_length=1000 )
    date_of_loan = forms.DateField( input_formats='%Y-%m-%d' )
    date_of_repayment = forms.DateField( input_formats='%Y-%m-%d' )

