from django.contrib import admin
from contacts.models import Contacts

class ContactsAdmin(admin.ModelAdmin):
	list_display = ('name','address')
	ordering = ['name']
	search_fields = ['name']

admin.site.register(Contacts, ContactsAdmin)
