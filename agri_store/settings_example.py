DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use 'django.db.backends.mysql' for MySQL
        'NAME': 'agri_store_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',  # default
    }
}

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('ar', 'العربية'),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True
