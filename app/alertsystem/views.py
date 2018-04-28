from django.shortcuts import render
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


def amber(request):
    context = {
        'title': "Amber Alert"
    }
    context['real_url'] = 'alertsystem:real_amber'
    context['real_image'] = 'alertsystem/Amber.png'
    context['test_url'] = 'alertsystem:test_amber'
    context['test_image'] = 'alertsystem/AmberTest.png'
    context['parent_url'] ='alertsystem:index'
    return render(request, 'alertsystem/real_or_test.html', context=context)


def real_amber(request):
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
    context['title'] = 'Real Amber Alert'
    context['message_type'] = 'real'
    context['image'] = 'alertsystem/Amber.png'
    context['parent_url'] = 'alertsystem:amber'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def test_amber(request):
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
    context['title'] = 'Test Amber Alert'
    context['message_type'] = 'test'
    context['image'] = 'alertsystem/AmberTest.png'
    context['parent_url'] = 'alertsystem:amber'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def natural(request):
    context = {
        'title': "Natural Disaster Threat"
    }
    return render(request, 'alertsystem/natural.html', context=context)


def tsunami(request):
    context = {
        'title': "Tsunami Threat"
    }
    context['real_url'] = 'alertsystem:real_tsunami'
    context['real_image'] = 'alertsystem/Tsunami2.png'
    context['test_url'] = 'alertsystem:test_tsunami'
    context['test_image'] = 'alertsystem/TsunamiTest.png'
    context['parent_url'] = 'alertsystem:natural'
    return render(request, 'alertsystem/real_or_test.html', context=context)


def real_tsunami(request):
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
    context['title'] = 'Real Tsunami Threat'
    context['message_type'] = 'real'
    context['image'] = 'alertsystem/Tsunami2.png'
    context['parent_url'] = 'alertsystem:tsunami'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def real_tsunami_sent(request):
    title = 'Real Tsunami Threat'
    name = 'WARNING: Real Tsunami Threat'
    message = 'Incoming tsunami on the shores of Waikiki. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)
    return render(request, 'alertsystem/sent.html', context=context)


def test_tsunami(request):
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
    context['title'] = 'Test Tsunami Threat'
    context['message_type'] = 'test'
    context['image'] = 'alertsystem/TsunamiTest.png'
    context['parent_url'] = 'alertsystem:tsunami'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def test_tsunami_sent(request):
    title = 'Test Tsunami Threat'
    name = 'TEST WARNING: Fake Tsunami Threat'
    message = 'THIS IS A DRILL. Incoming tsunami on the shores of Waikiki. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)
    return render(request, 'alertsystem/sent.html', context=context)


def hurricane(request):
    context = {
        'title': "Hurricane Threat"
    }
    context['real_url'] = 'alertsystem:real_hurricane'
    context['real_image'] = 'alertsystem/Hurricane.png'
    context['test_url'] = 'alertsystem:test_hurricane'
    context['test_image'] = 'alertsystem/HurricaneTest.png'
    context['parent_url'] = 'alertsystem:natural'
    return render(request, 'alertsystem/real_or_test.html', context=context)


def real_hurricane(request):
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
    context['title'] = 'Real Hurricane Threat'
    context['message_type'] = 'real'
    context['image'] = 'alertsystem/Hurricane.png'
    context['parent_url'] = 'alertsystem:hurricane'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def real_hurricane_sent(request):
    title = 'Real Hurricane Threat'
    name = 'WARNING: Real Hurricane Threat'
    message = 'Incoming hurricane from North Shore. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)
    return render(request, 'alertsystem/sent.html', context=context)


def test_hurricane(request):
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
    context['title'] = 'Test Hurricane Threat'
    context['message_type'] = 'test'
    context['image'] = 'alertsystem/HurricaneTest.png'
    context['parent_url'] = 'alertsystem:hurricane'
    context['form'] = form
    return render(request, 'alertsystem/confirmation.html', context=context)


def test_hurricane_sent(request):
    title = 'Test Hurricane Threat'
    name = 'TEST WARNING: Fake Hurricane Threat'
    message = 'THIS IS A DRILL. Incoming hurricane from North Shore. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)
    return render(request, 'alertsystem/sent.html', context=context)


def foreign(request):
    context = {
        'title': "Missile Threat"
    }
    context['real_url'] = 'alertsystem:real_foreign'
    context['real_image'] = 'alertsystem/missile.png'
    context['test_url'] = 'alertsystem:test_foreign'
    context['test_image'] = 'alertsystem/testMissile.png'
    context['parent_url'] ='alertsystem:index'
    return render(request, 'alertsystem/real_or_test.html', context=context)


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
    name = 'WARNING: Real Missile Threat'
    message = 'Incoming missile from North Korea. Seek immediate shelter on higher ground'
    context = _send_messages(title=title, name=name, message=message)

    return render(request, 'alertsystem/sent.html', context=context)


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

    return render(request, 'alertsystem/sent.html', context=context)


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

