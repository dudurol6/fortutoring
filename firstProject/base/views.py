from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') # Here, 'home.html' is rendered when user goes to home

def contact(request):
    return render(request, 'contact.html') # Here, 'contact.html' is rendered when user goes to contact

def http(request):
    return HttpResponse('This is how HttpResponse work.')