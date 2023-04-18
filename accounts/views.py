from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from GATE_website import views
from questionnaire.models import Joueur
from .forms import UserForm
from django.contrib.auth.decorators import login_required



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

@login_required
def moncompte(request):
    user = User.objects.all().filter(username=request.user.username)[0]
    context = {
        'user':user
    }
    return render(request, 'accounts/moncompte.html')


def supprimer_compte(request):
    joueur = Joueur.objects.all().filter(username=request.user.username)[0]
    user = User.objects.all().filter(username=request.user.username)[0]
    joueur.delete()
    user.delete()
    redirect(views.index)
    return render(request, 'GATE_website/index.html')


