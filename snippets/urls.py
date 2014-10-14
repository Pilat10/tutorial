from django.conf.urls import patterns, url
from snippets.views import snippet_list


urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', snippet_list, name='snip_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail')
)
