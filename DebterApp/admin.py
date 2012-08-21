# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class DebtAdmin(admin.ModelAdmin):
    fields = ['debtor', 'loaner', 'amount', 'date_of_loan', 'date_of_repayment', 'title', 'description']

admin.site.register(Debt, DebtAdmin)
