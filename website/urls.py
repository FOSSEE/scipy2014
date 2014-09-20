from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^page/$', 'website.views.page', name='page'),
    url(r'^venue/$', 'website.views.venue', name='venue'),
    url(r'^schedule/$', 'website.views.schedule', name='schedule'),
    url(r'^sponsors/$', 'website.views.sponsors', name='sponsors'),
    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^register/$', 'website.views.register', name='register'),
    url(r'^invited-speakers/$', 'website.views.invited_speakers', name='invited_speakers'),
    url(r'^call-for-proposals/$', 'website.views.call_for_proposals', name='call_for_proposals'),
    url(r'^call-for-proposals/(?P<action>[^/]+)$', 'website.views.call_for_proposals', name='call_for_proposals'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
