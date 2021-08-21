from django.urls import path
from .views import CreateProfile,logout_view,EditProfile,PasswordChangeView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path("register/",CreateProfile,name="registration"),
    path("login/",auth_views.LoginView.as_view(template_name='profiles/login.html',authentication_form=LoginForm,extra_context={"registration":True}),name="login"),
    path('logout/',logout_view,name="logout"),
    path('edit/',EditProfile.as_view(),name="edit"),
    path('password/',PasswordChangeView.as_view(template_name='profiles/changePassword.html'),name="update-password"),

]