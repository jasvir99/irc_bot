from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irc_bot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'irc_bot.bot.views.logPage'),
    url(r'^admin/', include(admin.site.urls)),
)
