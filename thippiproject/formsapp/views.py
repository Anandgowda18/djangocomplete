from django.shortcuts import render
from django.http import HttpResponse
from formsapp import forms

# Create your views here.
def check(request):
    return HttpResponse('<h1>the urls is set</h1>')
def userRegistrationForm(request):
    form = forms.UserRegistrationForm()
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("firstname:", form.cleaned_data['firstname'])
            print("lastname:", form.cleaned_data['lastname'])
            print("email:", form.cleaned_data['email'])
            print("gender:", form.cleaned_data['gender'])
            print("password:", form.cleaned_data['password'])
        else:
            print("something")
    else:
        print("nothing")
    return render(request,'formsapp/userregistration.html',{'form':form})