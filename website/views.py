from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    return render(request, 'website/templates/home.html', context_instance=RequestContext(request))

def page(request):
    return render(request, 'website/templates/page.html', context_instance=RequestContext(request))

def venue(request):
    return render(request, 'website/templates/venue.html', context_instance=RequestContext(request))
    
def contact(request):
    return render(request, 'website/templates/contact.html', context_instance=RequestContext(request))

def register(request):
    return render(request, 'website/templates/register.html', context_instance=RequestContext(request))
    
def schedule(request):
    return render(request, 'website/templates/schedule.html', context_instance=RequestContext(request))

def sponsors(request):
    return render(request, 'website/templates/sponsors.html', context_instance=RequestContext(request))

def invited_speakers(request):
    return render(request, 'website/templates/invited-speakers.html', context_instance=RequestContext(request))

def call_for_proposals(request):
    return render(request, 'website/templates/call-for-proposals.html', context_instance=RequestContext(request))
