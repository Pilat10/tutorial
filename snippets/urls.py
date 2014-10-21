from django.conf.urls import patterns, url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', views.SnippetList.as_view(), name='snip_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),
        name='snippet_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)