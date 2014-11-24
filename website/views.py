from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.template import RequestContext
from django.core.mail import send_mail

from website.forms import UserLoginForm, UserRegisterForm, ProposalForm, ContactUsForm
from website.models import Proposal, Comments

def home(request):
    return render(request, 'website/templates/home.html')

def page(request):
    return render(request, 'website/templates/page.html')

def venue(request):
    return render(request, 'website/templates/venue.html')
    
def contact(request):
    context = {}
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            from_email = form['useremail']
            to = ('scipy@fossee.in',)
            subject = form['subject'] + "-" + form['username']
            message = form['message']
            send_mail(subject, message, from_email, to, fail_silently=True)
            context['mailsent'] = True
            return render(request, 'website/templates/contact.html', context)
        else:
            context['form'] = form
            return render(request, 'website/templates/contact.html', context)
    form = ContactUsForm()
    context['form'] = form
    return render(request, 'website/templates/contact.html', context)


def register(request):
    return render(request, 'website/templates/register.html')
    
def schedule(request):
    return render(request, 'website/templates/schedule.html')

def sponsors(request):
    return render(request, 'website/templates/sponsors.html')

def invited_speakers(request):
    return render(request, 'website/templates/invited-speakers.html')

def UserLogout(request):
    user = request.user
    if user.is_authenticated() and user.is_active:
        logout(request)
    return HttpResponseRedirect('/')

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
        user = request.user
        if user.groups.filter(name='moderator').exists():
            return HttpResponseRedirect('/2014/cfp-view-abstracts')
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


def view_abstracts(request):
    user = request.user
    context = {}
    if user.is_authenticated():
        if user.groups.filter(name='moderator').exists():
            proposals = Proposal.objects.all()
            context['proposals'] = proposals
            context['user'] = user
            return render(request, 'website/templates/view-abstracts.html', context)
        else:
            return render(request, 'website/templates/prohibited.html')
    else:
        return render(request, 'website/templates/prohibited.html')


def abstract_details(request, proposal_id=None):
    user = request.user
    context = {}
    if user.is_authenticated():
        if user.groups.filter(name='moderator').exists():
            proposal = Proposal.objects.get(id=proposal_id)
            if request.method == 'POST':
                comment = Comments()
                comment.comment = request.POST['comment']
                comment.user = user
                comment.proposal = proposal
                comment.save()
                comments = Comments.objects.filter(proposal=proposal)
                context['proposal'] = proposal
                context['comments'] = comments
                context.update(csrf(request))
                return render(request, 'website/templates/abstract-details.html', context)
            comments = Comments.objects.filter(proposal=proposal)
            context['proposal'] = proposal
            context['comments'] = comments
            return render(request, 'website/templates/abstract-details.html', context)
        else:
            return render(request, 'website/templates/prohibited.html')
    else:
        return render(request, 'website/templates/prohibited.html')


def poster(request):
    return render(request, 'website/templates/poster.html')
