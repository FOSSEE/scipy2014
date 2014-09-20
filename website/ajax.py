from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form

from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from website.forms import UserLoginForm, UserRegisterForm, ProposalForm

@dajaxice_register
def user_login(request, form):
    if request.user.is_anonymous():
        dajax = Dajax()
        form = UserLoginForm(deserialize_form(form))
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = cleaned_data.get("user")
            login(request, user)
            dajax.remove_css_class('#login-form div', 'has-error')
            dajax.remove('.error-message')
            dajax.redirect('/call-for-proposals');
        else:
            dajax.remove_css_class('#login-form div', 'has-error')
            dajax.remove('.error-message')
            for item in form:
                dajax.add_css_class('#wrap_id_%s' % item.name, 'has-error')
            # non field errors
            if form.non_field_errors():
                message = '<div class="error-message alert alert-danger"><small>{0}</small></div>'.format(form.non_field_errors())
                dajax.append('#non-field-errors', 'innerHTML', message)
        return dajax.json()

@dajaxice_register
def user_logout(request):
    dajax = Dajax()
    logout(request)
    dajax.redirect('/call-for-proposals');
    return dajax.json()
    


@dajaxice_register
def user_register(request, form):
    dajax = Dajax()
    if request.user.is_anonymous():
        form = UserRegisterForm(deserialize_form(form))
        if form.is_valid():
            form.save()
            dajax.remove_css_class('#register-form div', 'has-error')
            dajax.remove('.error-message')
            dajax.redirect('/call-for-proposals')
        else:
            dajax.remove_css_class('#register-form div', 'has-error')
            dajax.remove('.error-message')
            for error in form.errors:
                dajax.add_css_class('#reg_wrap_id_%s' % error, 'has-error')
            for field in form:
                for error in field.errors:
                    message = '<div class="error-message">* {0}</div>'.format(error)
                    dajax.append('#reg_wrap_id_%s' % field.name, 'innerHTML', message) 
        return dajax.json()

@dajaxice_register
def submit_proposal(request, form):
    dajax = Dajax()
    form = ProposalForm(deserialize_form(form))
    if form.is_valid():
        print "########", valid
        form.save(commit=False)
        form.user = request.user
        form.save()
        dajax.remove_css_class('#proposal-form div', 'has-error')
        dajax.remove('.error-message')
    else:
        dajax.remove_css_class('#proposal-form div', 'has-error')
        dajax.remove('.error-message')
        for error in form.errors:
            dajax.add_css_class('#wrap_id_%s' % error, 'has-error')
        for field in form:
            for error in field.errors:
                message = '<div class="error-message">* {0}</div>'.format(error)
                dajax.append('#wrap_id_%s' % field.name, 'innerHTML', message) 
    return dajax.json()

@dajaxice_register
def test(request):
    return simplejson.dumps({'msg':'hello'})
