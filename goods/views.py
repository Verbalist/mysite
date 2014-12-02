from django.shortcuts import render
from django.views import generic

from goods.models import Goods

class IndexView(generic.ListView):
	template_name = 'goods/index.html'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Goods.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
	model = Goods
	template_name = 'goods/detail.html'
