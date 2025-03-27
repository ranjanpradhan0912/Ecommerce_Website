from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages


def register_view(request):

    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Hey{username},your account was successfully created")
            new_user=authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("core:index")

        else:
            print("Invalid form",form.errors)

       
    else:
        pass
    
    form=UserRegisterForm()
    
  
    return render(request,"userauths/sign-up.html",{"form":form})
