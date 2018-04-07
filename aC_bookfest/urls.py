from django.conf.urls import url
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
	  #url(r'^$', views.index, name='home'), (home page url)
    #url(r'^$', views.index, name='index'),
    
    
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.testhome, name='testhome'),
    url(r'^free/$', views.free, name='free'),
    # url(r'^accounts/login$', views.login, name='cas_ng_login'),
    # url(r'^accounts/logout$', views.logout, name='cas_ng_logout'),
    #url(r'^uploads/$', views.model_form_upload, name='model_form_upload'),
    # url(r'^signup/$', views.profile_create, name='profile_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ProfileUpdate.as_view(), name='profile_update'),
    url(r'^user/$', views.UserView, name='user'),

    url(r'^event/(?P<pk>\d+)/$', views.event_comment_create, name='event_detail'),
    url(r'^event/(?P<pk>\d+)/fav$', views.event_favorite, name='event_favorite'),
    url(r'^event/(?P<pk>\d+)/order$', views.event_order, name='event_order'),
    url(r'^event/(?P<pk>\d+)/checkin$', views.event_checkin, name='event_checkin'),

    # leave ranking feature later
    #url(r'^ranking/$', views.TopUsers, name='TopUsers'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)