# -*- coding: utf-8 -*-


"""Views.

Ten moduł odpowiedzialny jest za generowanie widoków stron.
Zawiera funkcje za to odpowiedzialne:

def index(request): widok strony głównej
def logout_view(request): ekran pożegnelny --- wyświetlany po wylogowaniu
def profil_d(request): wyświetla dane profilu użytkownika, pobiera jego stan długów i wierzytelności
def dlug(request): formularz służący dodaniu nowego wpisu do bazy
"""

import user

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth import logout

from form import *
from django.contrib.auth.models import User




def index(request):
    """
    def index - funkcja odpowiedzialna za zwrócenie strony głównej
    """
    return render_to_response('index.html', context_instance=RequestContext(request))


def logout_view(request):
    """
    def logout_view - funkcja odpowiedzialna za wylogowanie użytkownika
    """
    logout(request)
    return render_to_response('registration/logout.html', context_instance=RequestContext(request))

def profil_d(request):
    """
    def profil_d - odpowieda za wyłuskanie z bazy długów i wierzytelności użytkownika
    oraz wyświetlenie ekranu je zawierającego
    """
    title = "Debts"
    user = request.user
    debts = Debts.objects.filter(debtor = user)
    loans = Debts.objects.filter(loaner = user)
    return render_to_response('profil.html', locals())

def rejestracja(request):
    title = "Register_form"
    if request.method == 'POST':
        debt_proposition_form = NewDebtForm(request.POST)
        if debt_proposition_form.is_valid():
            form = debt_proposition_form
            Debts.objects.create_debt(form, request.user)
            debt_proposition_form = NewDebtForm()
    else:
        debt_proposition_form = NewDebtForm()
    return render_to_response('rejestracja.html', locals(), context_instance=RequestContext(request))


def dlug(request):
    """
    def dlug - funkcja odpowiedzialan za wyświetlenie formularza dodawania długu
    """
    title = "Debt"
    users = User.objects.all()
    if request.method == 'POST':
        debt_proposition_form = NewDebtForm(request.POST)
        if debt_proposition_form.is_valid():
            form = debt_proposition_form
            Debts.objects.create_debt(form, request.user)
            debt_proposition_form = NewDebtForm()
    else:
        debt_proposition_form = NewDebtForm()
    return  render_to_response('dlug.html', locals(), context_instance=RequestContext(request))


