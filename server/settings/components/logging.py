# Future logging configuration



_LOG_MSG_FORMAT = {'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:(lineno)d]'}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'default': _LOG_MSG_FORMAT},

    'handlers': {
        'info_console_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'error_console_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stderr',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['info_console_handler'],
            'propagate': True,
            'level': 'INFO',
        },
        'security': {
            'handlers': ['error_console_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['info_console_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
