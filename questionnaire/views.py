from django.shortcuts import render, redirect

from GATE_website.views import quizz
from .models import Joueur, ProtecDesDonneesLv1, ProtecDesDonneesLv2, ProtecDesDonneesLv3, MdpEtAuthLv1, MdpEtAuthLv2, MdpEtAuthLv3, ProtecContreLesMenacesLv1, ProtecContreLesMenacesLv2, ProtecContreLesMenacesLv3, HygienenumeriqueLV1, HygienenumeriqueLV2, HygienenumeriqueLV3


def quizzrep(request):
    if request.method == 'POST':
        return redirect(quizz)
    return render(request, "questionnaire/pddquizzrep.html")




def pddquizz1(request):
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
        return traitementdatapdd1(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)





def traitementdatapdd1(request, liste_rep_ok):
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

def pddquizz3(request):
    questions = ProtecDesDonneesLv3.objects.all()
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
        if joueur.qcmpdd3 < resultat:
            joueur.qcmpdd3 = resultat
            joueur.qcmpdd3pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepdd1 = True
            joueur.qcmpddTpourcentage = (joueur.qcmpdd1pourcentage+joueur.qcmpdd2pourcentage + joueur.qcmpdd3pourcentage)/3
            if joueur.qcmpddTpourcentage>75:
                joueur.validepddT = True
        joueur.save()
        return traitementdatapdd3(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatapdd3(request, liste_rep_ok):
    questions = ProtecDesDonneesLv3.objects.all()
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


def mdp1(request):
    questions = MdpEtAuthLv1.objects.all()
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
        if joueur.qcmmea1 < resultat:
            joueur.qcmmea1 = resultat
            joueur.qcmmea1pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepdd1 = True
            joueur.qcmpddTpourcentage = (joueur.qcmmea1pourcentage+joueur.qcmmea2pourcentage)/2
            if joueur.qcmmeaTpourcentage>75:
                joueur.validemeaT = True
        joueur.save()
        return traitementdatamdp1(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatamdp1(request, liste_rep_ok):
    questions = MdpEtAuthLv1.objects.all()
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


def pcm1(request):
    questions = ProtecContreLesMenacesLv1.objects.all()
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
        if joueur.qcmpcm1 < resultat:
            joueur.qcmpcm1 = resultat
            joueur.qcmpcm1pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepcm1 = True
            joueur.qcmpddTpourcentage = (joueur.qcmpcm1pourcentage1 + joueur.qcmpcm2pourcentage+ joueur.qcmpcm3pourcentage)/3
            if joueur.qcmpcmTpourcentage>75:
                joueur.validepcmT = True
        joueur.save()
        return traitementdatapcm1(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatapcm1(request, liste_rep_ok):
    questions = ProtecContreLesMenacesLv1.objects.all()
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


def pcm2(request):
    questions = ProtecContreLesMenacesLv2.objects.all()
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
        if joueur.qcmpcm2 < resultat:
            joueur.qcmpcm2 = resultat
            joueur.qcmpcm2pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepcm2 = True
            joueur.qcmpddTpourcentage = (joueur.qcmpcm1pourcentage1 + joueur.qcmpcm2pourcentage+ joueur.qcmpcm3pourcentage)/3

            if joueur.qcmpcmTpourcentage>75:
                joueur.validepcmT = True
        joueur.save()
        return traitementdatapcm2(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatapcm2(request, liste_rep_ok):
    questions = ProtecContreLesMenacesLv2.objects.all()
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

def pcm3(request):
    questions = ProtecContreLesMenacesLv3.objects.all()
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
        if joueur.qcmpcm3 < resultat:
            joueur.qcmpcm3 = resultat
            joueur.qcmpcm3pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepcm3 = True
            joueur.qcmpddTpourcentage = (joueur.qcmpcm1pourcentage1 + joueur.qcmpcm2pourcentage+ joueur.qcmpcm3pourcentage)/3

            if joueur.qcmpcmTpourcentage>75:
                joueur.validepcmT = True
        joueur.save()
        return traitementdatapcm3(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatapcm3(request, liste_rep_ok):
    questions = ProtecContreLesMenacesLv3.objects.all()
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

def hn1(request):
    questions = HygienenumeriqueLV1.objects.all()
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
        if joueur.qcmhn1 < resultat:
            joueur.qcmhn1 = resultat
            joueur.qcmhn1pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validehn1 = True
            joueur.qcmhnTpourcentage = (joueur.qcmhn1pourcentage + joueur.qcmhn2pourcentage+ joueur.qcmhn3pourcentage)/3

            if joueur.qcmhnTpourcentage>75:
                joueur.validehnT = True
        joueur.save()
        return traitementdatahn1(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatahn1(request, liste_rep_ok):
    questions = HygienenumeriqueLV1.objects.all()
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

def hn2(request):
    questions = HygienenumeriqueLV2.objects.all()
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
        if joueur.qcmhn2 < resultat:
            joueur.qcmhn2 = resultat
            joueur.qcmhn2pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validehn3 = True
            joueur.qcmhnTpourcentage = (joueur.qcmhn1pourcentage1 + joueur.qcmhn2pourcentage+ joueur.qcmhn3pourcentage)/3

            if joueur.qcmhnTpourcentage>75:
                joueur.validehnT = True
        joueur.save()
        return traitementdatahn2(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatahn2(request, liste_rep_ok):
    questions = HygienenumeriqueLV2.objects.all()
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

def hn3(request):
    questions = HygienenumeriqueLV3.objects.all()
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
        if joueur.qcmhn3 < resultat:
            joueur.qcmhn3 = resultat
            joueur.qcmhn3pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validehn3 = True
            joueur.qcmhnTpourcentage = (joueur.qcmhn1pourcentage1 + joueur.qcmhn2pourcentage+ joueur.qcmhn3pourcentage)/3

            if joueur.qcmhnTpourcentage>75:
                joueur.validehnT = True
        joueur.save()
        return traitementdatahn3(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatahn3(request, liste_rep_ok):
    questions = HygienenumeriqueLV3.objects.all()
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


def pddquizz2(request):
    questions = ProtecDesDonneesLv2.objects.all()
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
        if joueur.qcmpdd2 < resultat:
            joueur.qcmpdd2 = resultat
            joueur.qcmpdd2pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepdd2 = True
            joueur.qcmhnTpourcentage = (joueur.qcmpdd1pourcentage + joueur.qcmpdd2pourcentage+ joueur.qcmpdd3pourcentage)/3

            if joueur.qcmpddTpourcentage>75:
                joueur.validepddT = True
        joueur.save()
        return traitementdatapdd2(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatapdd2(request, liste_rep_ok):
    questions = ProtecDesDonneesLv2.objects.all()
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

def mdp2(request):
    questions = MdpEtAuthLv2.objects.all()
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
        if joueur.qcmmea2 < resultat:
            joueur.qcmmea2 = resultat
            joueur.qcmmea2pourcentage = resultat*100/final
            if (75*final/100<=resultat):
                joueur.validepdd2 = True
            joueur.qcmpddTpourcentage = (joueur.qcmmea1pourcentage+joueur.qcmmea2pourcentage)/2
            if joueur.qcmmeaTpourcentage>75:
                joueur.validemeaT = True
        joueur.save()
        return traitementdatamdp2(request, liste_reponses_ok)
    return render(request, "questionnaire/pddquizz.html", context)




def traitementdatamdp2(request, liste_rep_ok):
    questions = MdpEtAuthLv2.objects.all()
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
