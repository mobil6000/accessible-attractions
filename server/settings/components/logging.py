'''
Configuring the logging mechanism for the application
'''



_LOG_MESSAGE_FORMATTERS = {
    'default': {'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:(lineno)d]'},
}


_LOG_HENDLERS = {
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
}


_LOGGERS = {
    'django': {
        'handlers': ('info_console_handler',),
        'propagate': True,
        'level': 'INFO',
    },
    'security': {
        'handlers': ('error_console_handler',),
        'level': 'ERROR',
        'propagate': False,
    },
    'django.db.backends': {
        'handlers': ('info_console_handler',),
        'level': 'DEBUG',
        'propagate': False,
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': _LOG_MESSAGE_FORMATTERS,
    'handlers': _LOG_HENDLERS,
    'loggers': _LOGGERS,
}
