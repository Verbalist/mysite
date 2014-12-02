from django.shortcuts import render
from django.views import generic

from books.models import Books

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	#context_object_name = 'latest_contact_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Books.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
	model = Books
	template_name = 'books/detail.html'
