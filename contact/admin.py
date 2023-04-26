from django.contrib import admin
from .models import ContactModel


#admin.site.register(ContactModel)

@admin.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Mail','Objet', 'Message')
