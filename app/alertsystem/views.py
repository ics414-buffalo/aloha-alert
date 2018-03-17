from django.shortcuts import render
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
    send_text = ["SEND", "CONFIRM", "VERIFY", "ALERT"]
    context = {
        'title': "Real Missile Threat",
        'send_text': send_text[rand.randint(0, len(send_text) - 1)],
    }
    return render(request, 'alertsystem/real_foreign.html', context=context)


def real_foreign_sent(request):
    context = {
        'title': 'Real Missile Warning Sent'
    }
    return render(request, 'alertsystem/sent_threat.html', context=context)
