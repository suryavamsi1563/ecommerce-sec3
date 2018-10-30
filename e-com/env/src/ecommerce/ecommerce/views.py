from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    context = {
        "title":"Hey dude",
        "content":"Welcome to Home Page",
        "premiumcontent":"This is premium content"
    }
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":"Welcome to Home Page",
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Welcome to Home Page",
        "contactform":contact_form,
    }
    if contact_form.is_valid():
        print("Valid")
        print(contact_form.cleaned_data)
    else:
        print("Invalid")

    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"contact/view.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"loginform":form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            print(request.user.is_authenticated())
            context['loginform'] = LoginForm()
            return redirect('/')
        else:
            print("Error")
            context['loginform'] = LoginForm()
    return render(request,"auth/login.html",context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
        context['form'] = RegisterForm()
    return render(request,"auth/register.html",context)