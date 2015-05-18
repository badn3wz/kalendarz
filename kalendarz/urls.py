from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
import permission; permission.autodiscover()
from galeria.views import HomeView


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'kalendarz.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^cal/', include('cal.urls')),
	url(r'^gallery/', include('galeria.urls')),
	(r'^accounts/', include('allauth.urls')),
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^profile/', include('playerprofile.urls')),
	url(r'^streams/$', TemplateView.as_view(template_name='int_tv.html'), name='streams'),
	url(r'^youtube/$', TemplateView.as_view(template_name='int_yt.html'), name='youtube'),
	url(r'^squadxml/$', TemplateView.as_view(template_name='squad.xml', content_type='text/xml'), name='squadxml'),
	url(r'^servers/$', TemplateView.as_view(template_name='servers.html'), name='servers'),

)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)