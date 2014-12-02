from django.shortcuts import render
from django.views import generic

from contacts.models import Contacts

class IndexView(generic.ListView):
	template_name = 'contacts/index.html'
	#context_object_name = 'latest_contact_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Contacts.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
	model = Contacts
	template_name = 'contacts/detail.html'
