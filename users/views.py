from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

## Views file creates context to send the html file before presenting the information.
## this way we can use generalised statements in our html files and use the variable data created here

## When rendering our registere.html, we must send it a dictionary of data, where form = the form created.
## this way, in our register.html, we can reference form knowing the data will be sent from here.
def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required # Need to be logged in in order to see this profile url
def profile(request):
	if request.method =='POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid(): # if inputs are valid
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile') # must redirect to same page after submitting form to prevent hitting the render statement at the bottom

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	## The context we will be sending to the profile.html file.
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)