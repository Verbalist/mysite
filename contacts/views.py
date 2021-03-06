from django.shortcuts import render
from django.views import generic

from contacts.models import Contacts

class IndexView(generic.ListView):
	model = Contacts
	template_name = 'contacts/index.html'

class IndexViewPartner(generic.ListView):
	model = Contacts
	template_name = 'contacts/partners.html'

class DetailView(generic.DetailView):
	model = Contacts
	template_name = 'contacts/detail.html'

def about(request):
	return render(request, 'contacts/about.html')
