from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'authentication_form.html', {'form': register_form})