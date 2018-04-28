from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import AlertForm


SEND_TEXT = 'CONFIRM'
EMAIL = 'electronsean808@gmail.com'

BASE_CONTEXT = {
    'send_text': SEND_TEXT
}

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
    # If this is a POST request we, need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = AlertForm(request.POST, **{'send_text': SEND_TEXT})
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('sent')
    # If a GET (or any other method) we'll create a blank form
    else:
        form = AlertForm(**{'send_text': SEND_TEXT})
    context = BASE_CONTEXT
    context['title'] = 'Real Missile Threat'
    context['message_type'] = 'real'
    context['image'] = 'alertsystem/rocket2.png'
    context['parent_url'] = 'alertsystem:foreign'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def real_foreign_sent(request):
    title = 'Real Missile Threat'
    name = 'WARNING: Real Missle Threat'
    message = 'Incoming missile from North Korea. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)

    return render(request, 'alertsystem/sent_threat.html', context=context)


def test_foreign(request):
    # If this is a POST request we, need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = AlertForm(request.POST, **{'send_text': SEND_TEXT})
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('sent')
    # If a GET (or any other method) we'll create a blank form
    else:
        form = AlertForm(**{'send_text': SEND_TEXT})
    context = BASE_CONTEXT
    context['title'] = 'Test Missile Threat'
    context['message_type'] = 'test'
    context['image'] = 'alertsystem/testMissile.png'
    context['parent_url'] = 'alertsystem:foreign'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def test_foreign_sent(request):
    title = 'Test Missile Threat'
    name = 'TEST WARNING: Fake Missile Threat'
    message = 'THIS IS A DRILL. Incoming missile from North Korea. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)

    return render(request, 'alertsystem/sent_threat.html', context=context)


def _send_messages(title=None, name=None, message=None):
    # Sending Message to Emails (Works with valid emails to emails)
    send_mail(
        name,
        message,
        EMAIL,  # Add a Valid Email Here
        ['lenj@hawaii.edu'],  # Send to a list of Emails
    )
    # Sending Message to Phone Numbers (Works with valid numbers and emails)
    send_mail(
        name,
        message,
        EMAIL,  # Add a Valid Email Here
        ['8088409878@tmomail.net'],  # Send to a T-Mobile Phone Number
    )
    print("%s sent to all phones, news stations, televisions, radios, and sirens on Hawaii" % title)
    context = {
        'title': title,
        'name': name,
        'message': message,
    }

    return context

