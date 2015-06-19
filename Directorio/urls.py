from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views as appview
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Directorio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', appview.home, name="home"),
    url(r'^nueva-persona/$', appview.NuevaPersona.as_view(), name="nueva-persona"),
    url(r'^personas/$', appview.consultar_personas, name="personas"),
)
