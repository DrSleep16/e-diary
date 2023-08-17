from django.urls import path

from datacenter import views

urlpatterns = [
    path(r'^$', views.view_classes, name='classes'),
    path(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)$', views.view_class_info,
        name='class_info'),
    path(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)/schedule/$',
        views.view_schedule, name='schedule'),
    path(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)/schedule/$',
        views.view_schedule, name='schedule'),
    path(r'^schoolkid/(?P<schoolkid_id>[\w+ ]+)/$', views.view_schoolkid,
        name='schoolkid'),
    path(
        r'^journal/'
        r'(?P<year>[\w+ ]+)/'
        r'(?P<letter>[\w+ ]+)/'
        r'(?P<subject_id>[\w+ ]+)/$',
        views.view_journal, name='journal'),
]
