"""artistiCal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# CAS Authentication
# Source: https://github.com/mingchen/django-cas-ng
import django_cas_ng.views

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    url(r'', include('aC_bookfest.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/login/$', views.login, name='login', kwargs={'redirect_field_name': '~/'}),
    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^accounts/login$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^accounts/logout$', django_cas_ng.views.logout, name='cas_ng_logout'),
    
    url(r'^accounts/callback$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),

    # for every URL tshat starts with /, Django will find a corresponding view
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
