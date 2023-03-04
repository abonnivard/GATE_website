from django.shortcuts import render, redirect

from GATE_website.views import quizz
from .models import ProtecDesDonneesLv1, Joueur


def pddquizz(request):
    questions = ProtecDesDonneesLv1.objects.all()
    context = {
        'questions':questions
    }
    if request.method == 'POST':
        liste_reponses_ok = [False]*len(questions)
        liste_checkbox = request.POST.getlist('qcm1')
        resultat = 0
        final = len(questions)
        for question in questions:
            question_test = []
            if question.reponse == "null":
                nb = question.reponseVrai.count(";")
                compteur = 0
                i=0
                start = question.reponseVrai.index(":")
                end = question.reponseVrai.index(";")
                int_result = 0
                while compteur<nb:
                    question_test.append((f"{question.numero}"+"."+question.reponseVrai[i], float(question.reponseVrai[start+1:end])))
                    if f"{question.numero}"+"."+question.reponseVrai[i] in liste_checkbox:
                        int_result += float(question.reponseVrai[start+1:end])
                        i = end + 1

                    start = question.reponseVrai[start:].index(":") + start
                    end = question.reponseVrai[end:].index(";") +end
                    compteur+=1
                if int_result == 1:
                    resultat += 1
                    liste_reponses_ok[int(question.numero)-1] = True
                question_nb = []
                for k in question_test:
                    question_nb.append(k[0])
                compteur_point = 0
                for n in range(1,5):
                    if f'{question.numero}.{n}' in liste_checkbox and f'{question.numero}.{n}' not in question_nb:
                        for k in liste_checkbox:
                            if k in question_nb:
                                compteur_point += question_test[question_nb.index(k)][1]
                                del question_nb[question_nb.index(k)]
                if compteur_point !=0:
                    resultat -= compteur_point
                    liste_reponses_ok[int(question.numero) - 1] = False



            elif question.reponse == request.POST.get(f'{question.numero}'):
                resultat+=1
                liste_reponses_ok[int(question.numero)-1] = True

        joueur = Joueur.objects.get(username=request.user.username)
        if joueur.qcmpdd1 < resultat:
            joueur.qcmpdd1 = resultat
            joueur.qcmpdd1pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepdd1 = True
            joueur.qcmpddTpourcentage = (joueur.qcmpdd1pourcentage+joueur.qcmpdd2pourcentage + joueur.qcmpdd3pourcentage)/3
            if joueur.qcmpddTpourcentage>75:
                joueur.validepddT = True
        joueur.save()
        return traitementdata(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)



def pddquizzrep(request):
    if request.method == 'POST':
        print('ok')
        return redirect(quizz)
    return render(request, "questionnaire/pddquizzrep.html")


def traitementdata(request, liste_rep_ok):
    questions = ProtecDesDonneesLv1.objects.all()
    liste_checkbox = request.POST.getlist('qcm1')

    liste_rep = []
    for i in range(len(liste_rep_ok)):
        if liste_rep_ok[i] is True:
            liste_rep.append(f'{i+1}')
    liste = []
    for element in liste_checkbox:
        liste.append(f"{element}")


    context = {
        "questions":questions,
        'vrai':liste_rep,
        'liste_rep':liste,
    }
    return render(request, "questionnaire/pddquizzrep.html", context)
