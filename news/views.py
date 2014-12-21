from django.shortcuts import render
from django.views import generic

from news.models import News

class IndexView(generic.ListView):
	template_name = 'news/index.html'

	def get_queryset(self):
		"""Return the last five published questions."""
		return News.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = News
	template_name = 'news/detail.html'
