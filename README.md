# Predditors Alt Tracker

## Installation

First, create a virtual environment in whatever way you like. I use
`virtualenvwrapper` so I do the following:

    mkvirtualenv --python=python3.4 predds

This automatically activates the virtual environment. In the future, use `workon
predds` to activate it again. Then install the requirements using `pip`:

    pip install -r requirements.txt

Go to https://developers.eveonline.com/applications and create a new app. Set
the callback URL to `http://127.0.0.1:8000/complete/eveonline/` and make sure
you have the following scopes:

 * `characterLocationRead`
 * `esi-location.read_location.v1`
 * `esi-location.read_ship_type.v1`

Setup a configuration file (add the secret key and ID from the EVE developers
page):

    cp predds_tracker/settings/local.template.py predds_tracker/settings/local.py

Make the database with all the necessary tables and fill it with SDE data:

    python manage.py migrate
    python manage.py loaddata eve_sde/fixtures/map.json
    python manage.py loaddata eve_sde/fixtures/items.json

You should now be able to run a local server using the following command:

    python manage.py runserver

You can update all the information in the database with the following command. I
recommend making a cronjob without the force flag.

    python manage.py runcrons --force
