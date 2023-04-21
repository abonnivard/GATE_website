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
from django.urls import path

from .views import quizzrep, pddquizz1, pddquizz3, mdp1, pcm1, pcm2, pcm3, hn1, hn2, hn3

app_name = 'questionnaire'


urlpatterns = [
    path("pddquizz1/", pddquizz1, name='pddquizz1'),
    path("pddquizz3/", pddquizz3, name="pddquizz3"),
    path('pcm1/', pcm1, name="pcm1"),
    path('pcm2/', pcm2, name="pcm2"),
    path('pcm3/', pcm3, name="pcm3"),
    path('hn1/', hn1, name="hn1"),
    path('hn2/', hn2, name="hn2"),
    path('hn3/', hn3, name="hn3"),
    path('mdp&auth1/', mdp1, name="mdp1"),
    path("quizzrep/", quizzrep, name="quizzrep"),
]
