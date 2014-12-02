from django.shortcuts import render
from django.views import generic

from news.models import News

class IndexView(generic.ListView):
	template_name = 'news/index.html'
	#context_object_name = 'latest_contact_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return News.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
	model = News
	template_name = 'news/detail.html'
