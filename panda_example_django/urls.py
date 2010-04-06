from django.conf.urls.defaults import *
import config

urlpatterns = patterns('',
    url('^$', 'panda_example_django.views.index', name='panda_example_django.index'),
    url(r'^player/(?P<panda_video_id>.+)?$', 'panda_example_django.views.player', name='panda_example_django.player'),
    (r'^(panda_uploader/.*)$', 'django.views.static.serve', {'document_root': config.PANDA_EXAMPLE_DJANGO_MEDIA_ROOT}),
    (r'^(player\.swf)$', 'django.views.static.serve', {'document_root': config.PANDA_EXAMPLE_DJANGO_PLAYER_DIR}),
)
