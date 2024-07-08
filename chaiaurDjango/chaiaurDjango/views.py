from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse ("Hello, World! This is about page of  the Chaiaur Django application.")

def contact(request):
    return HttpResponse ("Hello, World! This is contact page of  the Chaiaur Django application.")