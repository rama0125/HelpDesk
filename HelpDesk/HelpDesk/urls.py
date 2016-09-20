"""
Definition of urls for HelpDesk.
"""
from django.conf.urls import url

from app import  views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#from datetime import datetime
#from django.conf.urls import patterns, url
#from app.forms import BootstrapAuthenticationForm

## Uncomment the next lines to enable the admin:
#from django.conf.urls import include
#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'app.views.home', name='home'),
#    url(r'^contact$', 'app.views.contact', name='contact'),
#    url(r'^about', 'app.views.about', name='about'),
#    url(r'^login/$',
#        'django.contrib.auth.views.login',
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title':'Log in',
#                'year':datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        'django.contrib.auth.views.logout',
#        {
#            'next_page': '/',
#        },
#        name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
    
#)
