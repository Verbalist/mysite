from django.contrib import admin
from workshops.models import Tools, Workshops

class WorkshopsAdmin(admin.ModelAdmin):
	exclude = ('pub_date','visites','buys',)
	list_display = ('name','date','good','visites','buys')
	ordering = ['date']
	save_as = True
	search_fields = ['good__name', 'name', 'date']

admin.site.register(Tools)
admin.site.register(Workshops, WorkshopsAdmin)
