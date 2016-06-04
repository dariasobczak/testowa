from django.shortcuts import render_to_response

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

# Create your views here.
