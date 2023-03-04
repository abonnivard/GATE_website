from django.contrib import admin

from .models import MdpEtAuthLv1, ProtecDesDonneesLv1, ProtecDesDonneesLv2, ProtecDesDonneesLv3, Joueur

# Register your models here.
admin.site.register(MdpEtAuthLv1)
admin.site.register(ProtecDesDonneesLv1)
admin.site.register(ProtecDesDonneesLv2)
admin.site.register(ProtecDesDonneesLv3)
admin.site.register(Joueur)