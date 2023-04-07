from django.contrib import admin

from .models import MdpEtAuthLv1, ProtecDesDonneesLv1, ProtecDesDonneesLv2, ProtecDesDonneesLv3, Joueur, ProtecContreLesMenacesLv3, ProtecContreLesMenacesLv2, ProtecContreLesMenacesLv1, MdpEtAuthLv2, MdpEtAuthLv3, HygienenumeriqueLV1, HygienenumeriqueLV2, HygienenumeriqueLV3

# Register your models here.
admin.site.register(ProtecDesDonneesLv1)
admin.site.register(ProtecDesDonneesLv2)
admin.site.register(ProtecDesDonneesLv3)
admin.site.register(Joueur)
admin.site.register(HygienenumeriqueLV1)
admin.site.register(HygienenumeriqueLV2)
admin.site.register(HygienenumeriqueLV3)
admin.site.register(MdpEtAuthLv1)
admin.site.register(MdpEtAuthLv2)
admin.site.register(MdpEtAuthLv3)
admin.site.register(ProtecContreLesMenacesLv1)
admin.site.register(ProtecContreLesMenacesLv2)
admin.site.register(ProtecContreLesMenacesLv3)
