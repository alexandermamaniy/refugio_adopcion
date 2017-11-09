

#encoding:utf-8

import os

# funcion para redireccionar una URL
from django.core.urlresolvers import reverse_lazy

RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'p254nb+3*&d(3golvpgtgu2%3rxvtw&bt56ghv49n+pr5n5^8h'


DEBUG = True

ALLOWED_HOSTS = []



#aniadimos nuestras 3 apps a nuestra variable INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.mascota',
    'apps.adopcion',
    'apps.usuario',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'refugio2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #definimos que la ruta base de los templates sera este directorio
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'refugio2.wsgi.application'

#configuramos nuestra BASE DE DATOS en mi caso con POSTGRESQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'refugio2',
        'USER':'nom_DB',
        'PASSWORD':'password_DB',
        'HOST':'localhost',
        'PORT':5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# definimos el leguaje del codigo, en mi caso BOLIVIA
LANGUAGE_CODE = 'es-BO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

#esta nos redirecciona, cuando un usuario se loguea correactamente hacia el home de nuestro proyecto
LOGIN_REDIRECT_URL = reverse_lazy('home')

#este nos redirecciona hacia la URL login cuando un usuario se desloguea
LOGOUT_REDIRECT_URL = reverse_lazy('login')

#configuraciones necesarias para enviar correos a los usuarios, en caso de querer recuperar
#su contrasenia
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 25

EMAIL_HOST_USER = 'correo@gmail.com'
EMAIL_HOST_PASSWORD = 'password_correo'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
