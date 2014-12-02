from django.contrib import admin
from goods.models import Bases, Colors, Technics, Materials, Holidays, Styles, Goods

class GoodsAdmin(admin.ModelAdmin):
	exclude = ('pub_date','visites','buys')
	list_display = ('name','pub_date','technic','count','visites')
	ordering = ['pub_date']
	save_as = True
	search_fields = ['name']


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Bases)
admin.site.register(Colors)
admin.site.register(Technics)
admin.site.register(Materials)
admin.site.register(Holidays)
admin.site.register(Styles)

