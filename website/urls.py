from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^page/$', 'website.views.page', name='page'),
    url(r'^venue/$', 'website.views.venue', name='venue'),
    url(r'^contact/$', 'website.views.contact', name='contact'),
)
