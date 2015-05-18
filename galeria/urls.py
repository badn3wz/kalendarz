from django.conf.urls import patterns, url
from galeria.views import AlbumList, PhotoList, PhotoCreate, PhotoDetail


urlpatterns = patterns('',
    url(r'^$', AlbumList.as_view(), name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', PhotoList.as_view(), name='photo_list'),
    url(r'^add_photo/$', PhotoCreate.as_view(), name='add_photo'),
	url(r'^photo/(?P<pk>\d+)/$', PhotoDetail.as_view(), name='photo_detail'),
)