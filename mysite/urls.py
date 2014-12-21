from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from contacts.views import IndexViewPartner
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^news/', include('news.urls', namespace="news")),
	url(r'^goods/', include('goods.urls', namespace="goods")),
	url(r'^contacts/', include('contacts.urls', namespace="contacts")),
	url(r'^workshops/', include('workshops.urls', namespace="workshops")),
	url(r'^books/', include('books.urls', namespace="books")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
