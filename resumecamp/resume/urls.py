from django.conf.urls import patterns, url

from resume import views

urlpatterns = patterns('',
    url(r'^view/(?P<username>\w+)/$', views.viewresume, name='viewresume'),
)
