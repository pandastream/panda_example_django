from django.conf.urls.defaults import *
import config

urlpatterns = patterns('',
    url('^$', 'panda_django_example.views.index', name='panda_django_example.index'),
    url(r'^player/(?P<panda_video_id>.+)?$', 'panda_django_example.views.player', name='panda_django_example.player'),
    (r'^(panda_uploader/.*)$', 'django.views.static.serve', {'document_root': config.PANDA_DJANGO_EXAMPLE_MEDIA_ROOT}),
    (r'^(player\.swf)$', 'django.views.static.serve', {'document_root': config.PANDA_DJANGO_EXAMPLE_MEDIA_ROOT}),
)
