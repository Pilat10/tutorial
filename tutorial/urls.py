from django.conf.urls import patterns, include, url
from django.contrib import admin
from snippets import urls as api_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('snippets.urls')),
    url(r'^api/v1/', include(api_urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
