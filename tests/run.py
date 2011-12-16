# -*- coding: utf-8 -*-

import sys, os
from django.conf import settings


test_settings = {
    'DATABASES':{
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'ROOT_URLCONF': 'test_app.urls',
    'INSTALLED_APPS': [
        'visits',
        'test_app',
    ],
    'MIDDLEWARE_CLASSES': [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'visits.middleware.CounterMiddleware',
    ]
}


if __name__ == '__main__':
    test_args = sys.argv[1:]

    current_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    sys.path.insert(0, current_path)
    if not settings.configured:
        settings.configure(**test_settings)

    if not test_args:
        test_args = ['test_app']
    
    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner(verbosity=2, interactive=True, failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)
