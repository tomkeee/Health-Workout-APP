from django.urls import path
from .views import CreateProfile,login_view,logout_view,EditProfile,PasswordChangeView

urlpatterns = [
    path("register/",CreateProfile,name="registration"),
    path("login/",login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('edit/',EditProfile.as_view(),name="edit"),
    path('password/',PasswordChangeView.as_view(template_name='profiles/changePassword.html'),name="update-password"),

]