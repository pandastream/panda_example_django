import os.path
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
try:
    import json
except ImportError:
    import simplejson as json
from panda import Panda
import settings
from settings import PANDA_DETAILS as cfg

panda = Panda(cloud_id=cfg['cloud_id'], secret_key=cfg['secret_key'], access_key=cfg['access_key'])

def index(request):

    access_details = panda.signed_params('POST', '/videos.json')
    access_details_json = json.dumps(access_details)
    return render_to_response('panda_example_django/index.html', {
        'panda_access_details': access_details_json,
        'panda_api_host': panda.api_host
    })


@csrf_exempt
def authorize_upload(request):

    params = json.loads(request.POST['payload'])

    upload = panda.post("/videos/upload.json", {
      "file_name": params['filename'],
      "file_size": params['filesize'],
      "profiles": "h264",
    })

    auth = {"upload_url": json.loads(upload)["location"]}
    return HttpResponse(json.dumps(auth), mimetype='application/json')


def player(request, panda_video_id):
    panda_video_id = panda_video_id or request.GET.get('panda_video_id')
    cloud_url = json.loads(panda.get("/clouds/%s.json" % cfg['cloud_id']))['url']
    panda_encodings = json.loads(panda.get("/videos/%s/encodings.json" % panda_video_id))
    encoding = None
    for i in panda_encodings:
        if i['profile_name'] == 'h264':
            thumbnails = []
            for j in range(7):
              thumbnails.append("%s%s_%i%s" % (cloud_url, i['path'], j+1, ".jpg"))

            encoding = i.copy()
            encoding['url'] = "%s%s%s" % (cloud_url, i['path'], i['extname'])
            encoding['thumbnails'] = thumbnails

    return render_to_response('panda_example_django/player.html', {
        'panda_video_id': panda_video_id,
        'panda_encodings_repr': repr(panda_encodings).replace(',', ',\n'),
        'encoding': encoding,
    })