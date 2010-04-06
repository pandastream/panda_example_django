from django.shortcuts import render_to_response
try:
    import json
except ImportError:
    import simplejson as json
from panda import Panda
import settings
from settings import PANDA_DETAILS as pd

panda = Panda(api_host=pd['api_host'], cloud_id=pd['cloud_id'], secret_key=pd['secret_key'], access_key=pd['access_key'])

def index(request):
    access_details = panda.signed_params('POST', '/videos.json')
    access_details_json = json.dumps(access_details)
    return render_to_response('panda_example_django/index.html', {
        'panda_access_details': access_details_json,
        'panda_api_host': panda.api_host
    })

def player(request, panda_video_id):
    video_id = panda_video_id or request.GET.get('panda_video_id')
    panda_encodings = json.loads(panda.get("/videos/%s/encodings.json" % video_id))
    panda_encoding = panda_encodings[0]
    encoding = None;
    if panda_encoding['status'] == 'success':
        encoding = {
            'id'     : panda_encoding['id'],
            'url'    : "http://%s.s3.amazonaws.com/%s%s" % (settings.PANDA_S3_BUCKET, panda_encoding['id'], panda_encoding['extname']),
            'width'  : panda_encoding['width'],
            'height' : panda_encoding['height'],
        }
    return render_to_response('panda_example_django/player.html', {
        'panda_video_id': video_id,
        'panda_encodings_repr': repr(panda_encodings).replace(',', ',\n').replace('{', '\n{'),
        'encoding': encoding,
    })