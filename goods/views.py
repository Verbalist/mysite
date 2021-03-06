import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.core import serializers


from goods.models import Goods, Bases, Technics, Colors, Holidays, Materials, Styles

class IndexView(generic.ListView):
	template_name = 'goods/index.html'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Goods.objects.order_by('name')[:5]

	



class DetailView(generic.DetailView):
	model = Goods
	template_name = 'goods/detail.html'

	
def getGoods(request, my_order):
	data =  serializers.serialize('json', Goods.objects.all())
	return HttpResponse(data, content_type="application/json")

def getMenu(request, my_order):
	data = '['
	data += serializers.serialize('json', Bases.objects.all()).strip(']').strip('[') + ','
	data += serializers.serialize('json', Technics.objects.all()).strip(']').strip('[') + ','
	data += serializers.serialize('json', Colors.objects.all()).strip(']').strip('[') + ','
	data += serializers.serialize('json', Holidays.objects.all()).strip(']').strip('[') + ','
	#data += serializers.serialize('json', Materials.objects.all()).strip(']').strip('[') + ','
	data += serializers.serialize('json', Styles.objects.all()).strip(']').strip('[') + ']'
	
	return HttpResponse(data, content_type="application/json")

