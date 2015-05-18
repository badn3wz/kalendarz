from django.conf.urls import patterns, url
from cal.views import EventList, EventDetail, EntryUpdate, EntryCreate, EntryDelete, MonthArchive, EventCreateView, EventUpdateView, Archive

urlpatterns = patterns('',
    url(r'^list$', EventList.as_view(), name='index'),
    url(r'^event/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),
    url(r'^entry/(?P<pk>\d+)/switch_to/(?P<to_id>\d+)/$', EntryUpdate.as_view(), name='entry_update'),
    url(r'^entry/add/(?P<to_id>\d+)/$', EntryCreate.as_view(), name='entry_add'),
    url(r'^entry/delete/(?P<pk>\d+)/$', EntryDelete.as_view(), name='entry_delete'),
    url(r'^archive/$', Archive.as_view(), name='archive'),
    url(r'^archieve/(?P<year>\d{4})/(?P<month>\d+)/$',
        MonthArchive.as_view(month_format='%m'),
        name="archive_month"),
    url(r'^event/add/$', EventCreateView.as_view(), name='event_add'),
    url(r'^event/(?P<pk>\d+)/edit$', EventUpdateView.as_view(), name='event_edit'),
)