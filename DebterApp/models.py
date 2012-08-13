# -*- coding: utf-8 -*-

"""
models.py -- moduł zawierający struktury danych zawartych w serwisie
"""

from django.db import models
from django.contrib.auth.models import User

class DebtManager(models.Manager):
    """
    class DebtManager - interfejs opowiedzialny za dostarczanie zapytań bazy danych do modelu Debts
    """

    def create_debt(self, new_data, user):
        """
        def create_debt() - funkcja tworząca dług i zapisująca go w bazie
        """
        data = new_data.cleaned_data
        debt = self.model(
            user = data['user'],
            title = data['title'],
            amount = data['amount'],
            date_of_loan = data['date_of_loan'],
            date_of_repayment = data['date_of_repayment'],
            description = data['description'],
            accepted = True
        )
        debt.save()
        return debt



class Debts(models.Model):
    """
    class Debts - model
    """
    debtor = models.ForeignKey(User, related_name=u'debts')
    loaner = models.ForeignKey(User, related_name=u'loans')
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Kwota')
    date_of_loan = models.DateField(verbose_name=u'Data pożyczki')
    date_of_repayment = models.DateField(verbose_name=u'Data zwrotu')
    title = models.CharField(max_length=10, verbose_name=u'Tytuł')
    description = models.TextField(blank=True, verbose_name='Opis')

    objects = DebtManager()

    def __unicode__(self):
        """

        """
        return u"%s - %s - %s - %s" % (self.debtor, self.loaner, self.amount, self.title)


