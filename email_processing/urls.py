from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('zojax.django.mailin',
    url(r'^mailinTransport$', 'transport.transport', name='mailin-transport'),
    url(r'^mailloader$', 'mailloader_views.loader', name='mailin-loader'),
)
