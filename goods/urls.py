from django.conf.urls import patterns, url

from goods import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(jsonGoods\d*)', views.getGoods, name='json'),
	url(r'^(jsonMenu\d*)', views.getMenu, name='json'),
)
