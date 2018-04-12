from django.conf.urls import url
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

    url(r'^$', views.home, name='home'),
    # url(r'^home/$', views.testhome, name='testhome'),
    url(r'^free/$', views.free, name='free'),
    url(r'^free_event/(?P<pk>\d+)/$', views.free_event_detail, name='free_event_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^user/$', views.user, name='user'),
 
    #url(r'^uploads/$', views.model_form_upload, name='model_form_upload'),
    # url(r'^signup/$', views.profile_create, name='profile_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ProfileUpdate.as_view(), name='profile_update'),
    

    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^event/(?P<pk>\d+)/fav$', views.event_favorite, name='event_favorite'),

    # url(r'^event/(?P<pk>\d+)/order$', views.event_order, name='event_order'),
    url(r'^event/(?P<pk>\d+)/claim$', views.claim, name='claim'),
    url(r'^event/(?P<pk>\d+)/checkin$', views.event_checkin, name='event_checkin'),

    # leave ranking feature later
    #url(r'^ranking/$', views.TopUsers, name='TopUsers'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)