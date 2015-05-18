from django.conf.urls import patterns, url
from playerprofile.views import ProfileUpdateView, ProfileView, OwnProfileView, OwnProfileUpdateView, UserList, MemberList

urlpatterns = patterns('',
    url(r'^update/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='update_profile'),
    url(r'^(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile'),
    url(r'^own/$', OwnProfileView.as_view(), name='view_own_profile'),
    url(r'^update/own/$', OwnProfileUpdateView.as_view(), name='update_own_profile'),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^members/$', MemberList.as_view(), name='member_list'),
)