Panda example application, Django
=================================

An example Django web app that uses [**Panda**](http://www.pandastream.com) to encode videos and play them on a page.

Setup
-----

By default, Panda will encode your videos using the H.264 codec, playable with the HTML5 `<video>` tag. This example will use this to play your videos. Make sure you use a compatible browser to watch it.

This application has been tested successfully with **Python 2.5 and 2.6**. Make sure of the following:

Inside `settings.py`, you need to specify your Panda account details like follows:

    PANDA_DETAILS = {
      'api_host'   : 'api.pandastream.com',
      'cloud_id'   : 'your-cloud-id',
      'access_key' : 'your-access-key',
      'secret_key' : 'your-secret-key',
    }

Install the dependencies. We advise you to use `virtual_env`

    python setup.py develop

Run the server

    python manage.py runserver 8080

What does this do anyway?
-------------------------

The application will initially show a simple form where you can specify a video file to upload from your computer. Once uploaded, it will ask you to wait a bit until all is encoded. You'll have to reload the page yourself until this is done.

Finally, the video will appear embedded on the page. If you wish to try again with another video, a link is provided to restart the process.
