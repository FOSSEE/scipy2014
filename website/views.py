from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def home(request):
    return render(request, 'website/templates/home.html')

def page(request):
    return render(request, 'website/templates/page.html')
