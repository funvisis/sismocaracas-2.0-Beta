from django.conf.urls.defaults import patterns, include, url

from django.contrib import auth
from django.contrib import admin

from fvisusers.models import FVISUser


admin.site.register(FVISUser)
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^inspeccionesedificios/', include('funvisis.buildinginspections.urls')),
    url(r'^inspeccionespuentes/', include('funvisis.bridgeinspections.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),
    )
