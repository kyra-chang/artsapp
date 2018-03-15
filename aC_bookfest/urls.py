from django.conf.urls import url
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^home/$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^signup/$', views.profile_create, name='profile_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ProfileUpdate.as_view(), name='profile_update'),
    url(r'^user/$', views.UserView, name='user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)