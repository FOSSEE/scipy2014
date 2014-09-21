from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserLoginForm, UserRegisterForm, ProposalForm
from website.models import Proposal

def home(request):
    return render(request, 'website/templates/home.html')

def page(request):
    return render(request, 'website/templates/page.html')

def venue(request):
    return render(request, 'website/templates/venue.html')
    
def contact(request):
    return render(request, 'website/templates/contact.html')

def register(request):
    return render(request, 'website/templates/register.html')
    
def schedule(request):
    return render(request, 'website/templates/schedule.html')

def sponsors(request):
    return render(request, 'website/templates/sponsors.html')

def invited_speakers(request):
    return render(request, 'website/templates/invited-speakers.html')

def call_for_proposals(request, action=None):
    context = {}
    """ EDIT PROPOSAL SECTION """
    if action == 'edit':
        # POST
        if request.method == "POST":
            if request.user.is_authenticated():
                proposal = Proposal.objects.get(user=request.user)
                form = ProposalForm(request.POST, request.FILES, instance=proposal)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.user = request.user
                    data.save()
                    return HttpResponseRedirect('/2014/call-for-proposals')
                else:
                    context['proposal_form'] =  form
                    context['edit'] = True
                    return render(request, 'website/templates/call-for-proposals.html', context)
        # GET
        if Proposal.objects.filter(user=request.user).exists():
            proposal = Proposal.objects.get(user=request.user)
            context['proposal_form'] = ProposalForm(instance=proposal)
            context['edit'] = True
            return render(request, 'website/templates/call-for-proposals.html', context)
        else:
            return HttpResponseRedirect('/2014/call-for-proposals')
        # GET

    """ NEW PROPOSAL SECTION """
    # POST
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = ProposalForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.save()
            else:
                context['proposal_form'] =  form
                return render(request, 'website/templates/call-for-proposals.html', context)
    # GET
    if request.user.is_authenticated():
        # Checking whether proposal exists
        if Proposal.objects.filter(user=request.user).exists():
            context['proposal'] = Proposal.objects.get(user=request.user)
        else:
            context['proposal_form'] =  ProposalForm()
    else:
        context['login_form'] = UserLoginForm()
        context['register_form'] = UserRegisterForm()
    context.update(csrf(request))
    return render(request, 'website/templates/call-for-proposals.html', context)
