from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import *
from openlpwebapp.songs import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^openlpwebapp/', include('openlpwebapp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^$', views.search_songs),
    url(r'^home$', views.search_songs, name="home"),
    url(r'^lyrics/(\d+)$', views.song_lyrics, name="lyrics"),    
)
