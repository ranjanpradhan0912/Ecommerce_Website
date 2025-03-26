from django.shortcuts import render
from userauths.forms import UserRegisterForm

# Create your views here.

def register_view(request):

    if request.method== "POST":
        print("User registered successfully")
    else:
        print("User cannot be registered")
 
    form=UserRegisterForm()
  
    return render(request,"userauths/sign-up.html",{"form":form})
