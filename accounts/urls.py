"""GATE2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.urls import path

from GATE_website.views import index
from .forms import UserLoginForm
from .views import register

app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="accounts/logout.html", next_page=index), name='logout'),
    path('register/', register, name='register')
]
