Panda example application, Django
=================================

An example Django web app that uses [**Panda**](http://beta.pandastream.com) to encode videos and play them on a page.

Also available:

* the simple [Python Panda client library](http://github.com/newbamboo/panda_client_python) that this application is based on
* the also simple [Panda jQuery plugin](http://github.com/newbamboo/panda_uploader) used to upload files


Setup
-----

This application has been tested successfully with **Python 2.5 and 2.6**. Make sure of the following:

### 0. Create a Django project

This example runs as a Django app in an already existing Django project. If you don't have a project already, simply start one with:

    django-admin.py startproject myproject

### 1. Include this application in your project

The simplest way to install this application is as a Python package, using `easy_install` or `pip`:

    pip install panda_example_django

Then edit your settings.py and add this application to the INSTALLED_APPS tuple. For example:

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'panda_example_django', # This is the important line
    )

### 2. Account details

Again on `settings.py`, you need to specify your Panda account details like follows:

    PANDA_DETAILS = {
      'api_host'   : 'api.pandastream.com',
      'cloud_id'   : 'your-cloud-id',
      'access_key' : 'your-access-key',
      'secret_key' : 'your-secret-key',
    }
    PANDA_S3_BUCKET = 'panda-test-videos'


### 3. Routes to your app

Let Django know where the app is located using urls.py. A simple example would be:

    urlpatterns = patterns('',
        (r'', include('panda_example_django.urls')), # This is the important line
    )

### 4. The video player

This package does not include a video player. The one that this application uses is [JW Player](http://www.longtailvideo.com/players/jw-flv-player/) by Longtail. However, it has a restrictive license that does not allow us to distribute it along with the rest of the files.

Instead, you need to go to their website at http://www.longtailvideo.com, download the player, and copy the **player.swf** somewhere in your computer.

One this is done, edit `settings.py` so that the `PANDA_EXAMPLE_DJANGO_PLAYER_DIR` points to the **directory** (not the file) where the file `player.swf` is.

For example, if you just drop the file player.swf in the same directory where `settings.py` resides, you can simply do:

    PANDA_EXAMPLE_DJANGO_PLAYER_DIR = os.path.dirname(__file__)


And that should be all.


What does this do anyway?
-------------------------

The application will initially show a simple form where you can specify a video file to upload from your computer. Once uploaded, it will ask you to wait a bit until all is encoded. You'll have to reload the page yourself until this is done.

Finally, the video will appear embedded on the page, using a Flash player. If you wish to try again with another video, a link is provided to restart the process.


Notes
-----

Uploads are done using [SWFUpload](http://www.swfupload.org/).