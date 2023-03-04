from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from GATE_website import views
from questionnaire.models import Joueur
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            username = request.POST['username']
            user = authenticate(request, email=email, password=password, username=username)
            if user is not None:
                login(request, user)
                new = Joueur(username=username)
                new.save()
            if request.user.is_authenticated:
                return redirect(views.quizz)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
