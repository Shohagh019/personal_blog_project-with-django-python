from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from . import forms
def register(request):
    if request.method =='POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully!' )
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()    

    return render(request, 'register_form.html', {'form': register_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_password)
            if user is not None:
                messages.success(request, 'Logged in Successfully!' )
                login(request, user)
                return redirect('home')
        else:
            messages.warning(request, 'Login Information is Incorrect' )
            return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'login_form.html', {'form': form, 'type':'Login'})
    
@login_required    
def profile(request):
    data = Post.objects.filter(author = request.user)   

    return render(request, 'profile_form.html', {'data':data}) 
@login_required
def user_update(request):
    if request.method =='POST':
        profile_form = forms.UserUpdateForm(request.POST, instance= request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Account Updated Successfully!' )
            return redirect('profile')
    else:
        profile_form = forms.UserUpdateForm(instance= request.user)    

    return render(request, 'update_profile.html', {'form': profile_form}) 

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! Prevents logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Replace with your desired URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'password_change_form.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
           