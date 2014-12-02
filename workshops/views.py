from django.shortcuts import get_object_or_404
from django.views import generic

from goods.models import Goods
from workshops.models import Workshops

class IndexView(generic.ListView):
	template_name = 'workshops/index.html'
	#context_object_name = 'latest_contact_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Workshops.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
	model = Workshops
	#importGood = get_object_or_404(Goods, pk=request.GET)
	template_name = 'workshops/detail.html'
