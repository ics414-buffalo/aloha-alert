from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import AlertForm
import random as rand


# Create your views here.
def index(request):
    context = {
        'title': "Aloha Alert"
    }
    return render(request, 'alertsystem/index.html', context=context)

def foreign(request):
    context = {
        'title': "Missile Threat"
    }
    return render(request, 'alertsystem/foreign.html', context=context)


def real_foreign(request):
    send_text = "CONFIRM"
    # if this is a POST request we,  need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = AlertForm(request.POST, **{'send_text': send_text})
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('sent')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlertForm(**{'send_text': send_text})
    context = {
        'title': "Real Missile Threat",
        'send_text': send_text,
        'validation_form': form,
    }
    return render(request, 'alertsystem/real_foreign.html', context=context)


def real_foreign_sent(request):
    context = {
        'title': 'Real Missile Threat'
    }
    # Sending Message to Emails (Works with valid emails to emails)
    send_mail(
        'WARNING: Real Missle Threat',
        'Incoming missile from North Korea. Seek immediate shelter on higher ground',
        'example@gmail.com',  # Add a Valid Email Here
        ['secondexample@gmail.com'],  # Send to a list of Emails
    )
    # Sending Message to Phone Numbers (Works with valid numbers and emails)
    send_mail(
        'TEST WARNING: Fake Missle Threat',
        'Test for incoming missle from North Korea',
        'example@gmail.com',  # Add a Valid Email Here
        ['phonenumber@tmomail.net'],  # Send to a T-Mobile Phone Number
    )
    return render(request, 'alertsystem/sent_threat.html', context=context)


def test_foreign(request):
    send_text = "CONFIRM"
    # if this is a POST request we,  need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = AlertForm(request.POST, **{'send_text': send_text})
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('sent')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlertForm(**{'send_text': send_text})
    context = {
        'title': "Test Missile Threat",
        'send_text': send_text,
        'validation_form': form,
    }
    return render(request, 'alertsystem/test_foreign.html', context=context)


def test_foreign_sent(request):
    context = {
        'title': 'Test Missile Threat'
    }
    # Sending Message to Emails (Works with valid emails to emails)
    send_mail(
        'WARNING: Real Missle Threat',
        'Incoming missile from North Korea. Seek immediate shelter on higher ground',
        'example@gmail.com',  # Add a Valid Email Here
        ['secondexample@gmail.com'],  # Send to a list of Emails
    )
    # Sending Message to Phone Numbers (Works with valid numbers and emails)
    send_mail(
        'TEST WARNING: Fake Missle Threat',
        'Test for incoming missle from North Korea',
        'example@gmail.com', # Add a Valid Email Here
        ['phonenumber@tmomail.net'], # Send to a T-Mobile Phone Number
     )
    print("Message sent to all Phones on Hawaii")
    return render(request, 'alertsystem/sent_threat.html', context=context)
