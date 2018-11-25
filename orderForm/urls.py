"""orderForm URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from security.views import not_found_view
from extras.views import download
from extras.views import download_gps
from extras.views import download_vhf

urlpatterns = [
    url(r'^survey/', include('survey.urls', namespace='survey')),
    url(r'^vertex_lite/', include('vertexLite.urls', namespace='vertexLite')),
    url(r'^miniFawn/', include('miniFawn.urls', namespace='miniFawn')),
    url(r'^trapTransmitter/', include('traptransmitter.urls', namespace='trapTransmitter')),
    url(r'^admin/', admin.site.urls),
    url(r'^download/(?P<path>.*)/(?P<name>.*)/(?P<file>.*)', download, name='download'),
    url(r'^download_gps_schedule/(?P<path>.*)/(?P<name>.*)/(?P<file>.*)', download_gps, name='download_gps'),
    url(r'^download_vhf_schedule/(?P<path>.*)/(?P<name>.*)/(?P<file>.*)', download_vhf, name='download_vhf'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = not_found_view
handler500 = not_found_view