from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^', include('website.urls', namespace='website')),
    url(r'^admin/', include(admin.site.urls)),

    # Dajaxice urls
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # For devel
    # url(r'^2014/', include('website.urls', namespace='website')),
)
