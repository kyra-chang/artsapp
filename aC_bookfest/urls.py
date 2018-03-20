from django.conf.urls import url
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    #url(r'^uploads/$', views.model_form_upload, name='model_form_upload'),
    url(r'^signup/$', views.profile_create, name='profile_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ProfileUpdate.as_view(), name='profile_update'),
    url(r'^user/$', views.UserView, name='user'),
    url(r'^event/(?P<pk>\d+)/$', views.event_comment_create, name='event_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)