from common import *

DEBUG=True

INSTALLED_APPS += (
    'debug_toolbar',
)


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    #'HIDE_DJANGO_SQL': False,
    #'TAG': 'div',
    'ENABLE_STACKTRACES': True,
    #'HIDDEN_STACKTRACE_MODULES': ('gunicorn', 'newrelic'),
    'SHOW_TEMPLATE_CONTEXT': True,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
BASE_URL='http://localhost:8000/'

SECRET_KEY = 'dpc)c$h^0+&q&m=tn&%ey0)-wa+c&)odp5bv*7x9u4df4ef#h_'
