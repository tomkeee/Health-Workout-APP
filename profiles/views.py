from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from .forms import LoginForm, RegisterForm,EditProfileForm,ChangePasswordForm
from.models import Profile
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.views.generic import UpdateView

def logout_view(request):
    logout(request)
    return redirect('/profile/login')

def login_view(request):
    error_message=None
    form_b= LoginForm(request.POST or None)
    print(request.user)

    registration=True

    if request.method=="POST":
            if form_b.is_valid():
                username=form_b.cleaned_data.get("username")
                password=form_b.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect('/')
            else:
                error_message="Ups ... something went wrong"
        # else:
            # return HttpResponse("Validation error has occured")
        
    context={
        'form':form_b,
        'error_message':error_message,
        "registration":registration
    }
    return render(request,"profiles/login.html",context)


def CreateProfile(request):
    registration=True

    form=RegisterForm(request.POST or None)
    template_type="Registration"
    if form.is_valid():
        print("Is valid")
        print(request.user)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password2")
        email=""

        try:
            user=User.objects.create_user(username,email,password)
            print("CREATED")
        except:
            print("NOT CREATED")
            user=None
        if user != None:
            print("USER NONOE")
            login(request,user)
            return redirect("/")
        else:
            print("FORM NOT VALID")
            request.session['register_error']=1
    else:
        print("Not Valid")
    return render(request,"profiles/register.html",{"form":form, "registration":registration})


class EditProfile(UpdateView):
    form_class=EditProfileForm
    template_name="profiles/edit.html"
    success_url='/'

    def get_object(self):
        return self.request.user

class ChangePassword(UpdateView):
    form_class=ChangePasswordForm
    success_url=("/")

    def get_object(self):
        return self.request.user

def LookView(request):
    user=request.user
    print(user)
    profile=Profile.objects.filter(account=user)
    for instance in profile:
        time=instance.weight_starting
        print(time)

    weight=profile.values()
    weight2=profile.values_list()
    print(profile)
    print(weight)
    print(weight2)
    print(time)
    return HttpResponse("yeaah")