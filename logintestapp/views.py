from django.shortcuts import render_to_response,render
from django.views import generic
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from logintestapp.forms import SignUpForm,LoginForm
from django.contrib import messages

# Create your views here.

#class HomePageView(TemplateView):
#	def get(self, request, **kwargs):
#		return render(request, 'index.html', context=None)

def register(request):
	if request.method == 'POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			email= form.cleaned_data.get('email')
            
			return HttpResponseRedirect('/books/')
	else:
		form=SignUpForm()
	arg={'form':form}
	return render(request,'signup.html',arg)

def login(request):
    if request.user.is_authenticated :
        return render(request,"loggedin.html")

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'form' : form}
        if user is not None:
            auth.login(request,user)
            request.session.set_expiry(3600)
            request.session['user_id']=user.id
            request.session['username']=user.username
            if user.is_active:
                return HttpResponseRedirect('/books/')
        else:
            messages.error(request,'Username or Password Incorrect')
            return HttpResponseRedirect('/logintestapp/login/')
    else:
    	form = LoginForm()
    arg={'form':form}
    return render(request, "login.html", arg)

def confirmlogout(request):
    if request.session.get('user_id'):
        return render(request, "logout.html")
    else:
        return HttpResponseRedirect('/books/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/books/')