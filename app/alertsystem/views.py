from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'alertsystem/index.html')

def foreign(request):
    return render(request, 'alertsystem/foreign.html')