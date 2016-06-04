from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    
    userObject = User.objects.get(username=username)
    
    if user is not None and userObject.groups.filter(name='rodzice').exists():
            auth.login(request, user)
            return HttpResponseRedirect('/rodzic/loggedin')
    elif user is not None and userObject.groups.filter(name='opiekunowie').exists():     
        auth.login(request, user)
        return HttpResponseRedirect('/opiekun/loggedin')
    else:
        return HttpResponseRedirect('/rodzic/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


    
# Create your views here.
