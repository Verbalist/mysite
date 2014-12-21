from django.conf.urls import patterns, url

from contacts import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^partners/$', views.IndexViewPartner.as_view(), name='partners'),
	url(r'^about/$', views.about, name='partners'),
)
