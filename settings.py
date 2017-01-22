import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'predds'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'predds_tracker',
    'eve_sde'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'predds_tracker.pipeline.single_association',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

ROOT_URLCONF = 'predds_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'predds_tracker.wsgi.application'

AUTH_USER_MODEL = 'predds_tracker.Character'
AUTHENTICATION_BACKENDS = ('social_core.backends.eveonline.EVEOnlineOAuth2',)
SOCIAL_AUTH_EVEONLINE_SCOPE = ['characterLocationRead', 'esi-location.read_location.v1', 'esi-location.read_ship_type.v1']
SOCIAL_AUTH_EVEONLINE_KEY = ''
SOCIAL_AUTH_EVEONLINE_SECRET = ''
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/eveonline/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

STATIC_URL = '/static/'
