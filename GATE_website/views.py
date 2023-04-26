from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from questionnaire.models import Joueur


def index(request):
    context = {
        "connected":request.user.is_authenticated
    }
    return render(request, "GATE_website/index.html", context)


@login_required
def quizz(request):
    context = {
        'joueur': Joueur.objects.get(username=request.user.username)
    }
    return render(request, "GATE_website/quizz.html", context)

@login_required
def documentation(request):
    return render(request, "GATE_website/documentation.html")


def cgu(request):
    return render(request, "GATE_website/cg.html")