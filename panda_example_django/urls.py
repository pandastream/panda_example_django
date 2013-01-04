from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^videos/(?P<panda_video_id>.+)?$', 'panda_example_django.views.player', name='panda_example_django.player'),
    url('^$', 'panda_example_django.views.index', name='panda_example_django.index'),
    url(r'^panda/authorize_upload$', 'panda_example_django.views.authorize_upload'),
)