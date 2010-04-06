import os
import settings

try:
    PANDA_DJANGO_EXAMPLE_MEDIA_ROOT = settings.PANDA_DJANGO_EXAMPLE_MEDIA_ROOT
except AttributeError:
    PANDA_DJANGO_EXAMPLE_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
