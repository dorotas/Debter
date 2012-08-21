from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'DebterApp.views.index', name='index'),
    url(r'^index$', 'DebterApp.views.index', name='index'),

    #url(r'^logowanie$', 'django.contrib.auth.views.login', kwargs={'template_name': 'registration/login.html'}, name='login'),
    #url(r'^logout$', 'DebterApp.views.logout_view', name='logout'),

    #url(r'^rejestracja$', 'DebterApp.views.rejestracja', name='rejestracja'),

    url(r'^profile$', 'DebterApp.views.profil_d', name='profil'),

    url(r'^debt$', 'DebterApp.views.dlug', name='dlug'),

    url(r'^account/', include('registration.backends.default.urls')),

    # note, that this should be disabled for production code
    # (may be disabled outside of django, though)
    (r'^templates/(.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__), 'templates')}),


)


