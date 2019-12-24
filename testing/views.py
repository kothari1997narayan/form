
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.template.context import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import UserProfile

def new_user(request):
    # if request.method =='POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return render(request,'display_user.html',{'user': user})
    # else:
    #     form = RegistrationForm()
    #     return render(request, 'new_user.html', {'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            userprofile = UserProfile.objects.get(user = user)
            userprofile.image = form.cleaned_data.get('image')
            userprofile.save()
            return redirect('display_user')
    else:
        form = RegistrationForm()
    return render(request, 'new_user.html', {'form': form})

def display_user(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    userprofile = UserProfile.objects.get( user = user)
    return render(request, 'display_user.html', {'user': user ,'userprofile': userprofile})


def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    userprofile = UserProfile.objects.get( user = user)
    return render(request, 'display_user.html', {'user': user ,'userprofile': userprofile})