from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
	exclude = ('pub_date',)
	list_display = ('name','pub_date')
	ordering = ['pub_date']
	save_as = True
	search_fields = ['workshop__name']

admin.site.register(News, NewsAdmin)
