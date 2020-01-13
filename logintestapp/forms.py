from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model

class SignUpForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Username',
			}
		))
	password1 = forms.CharField(widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
			}
		))
	password2 = forms.CharField(widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Re-enter Password',
			}
		))
	email=forms.EmailField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Email-ID',
			}
		))
	error_css_class = "error"

#	contact=forms.CharField(widget=forms.NumberInput(
#			attrs={
#				'placeholder': 'Contact No.',
#			}
#		))
#	gender=forms.ChoiceField(widget=forms.RadioSelect(),
#			choices=(
#			('male', 'Male'),
#			('female', 'Female'),
#			))

	class Meta:
		model=User
		fields=('username', 'password1', 'email')

	def save(self,commit=True):
		user=super(SignUpForm,self).save(commit=False)
#		user.email= form.cleaned_data.get('email')
#		user.contact= form.cleaned_data.get('contact')
#		user.gender= form.cleaned_data.get('gender')
		if(commit):
			user.save()
		return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
	    username = self.cleaned_data.get("username")
	    password = self.cleaned_data.get("password")
	    if username and password:
	        user = authenticate(username=username, password=password)
	        if not user:
	            raise forms.ValidationError("User does not exist.")
	        if not user.is_active:
	            raise forms.ValidationError("User is no longer active.")
	    return super(LoginForm, self).clean(*args, **kwargs)