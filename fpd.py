#!/bin/env python
# Create the basic directory structure for
# your Flask based projects.

import os, sys

# Few core directories
app_dirs = (
    'app/templates',
    'app/static',
    'app/main',
    'api',
    'migrations',
    'tests',
    'venv'
)
# Main config files for the project
app_files = (
    'app/main/__init__.py',
    'app/main/errors.py',
    'app/main/forms.py',
    'app/main/views.py',
    'app/__init__.py',
    'app/models.py',
    'tests/__init__.py',
    'tests/test.py',
    'requirements.txt',
    'config.py',
    'manage.py'
)

def struct_app(app_name):
    # First create dirs
    for e in app_dirs:
        os.makedirs(os.path.abspath('%s/%s' % (app_name, e)))

    # Now create files
    for f in app_files:
        with open(os.path.abspath('%s/%s' % (app_name, f)), 'w') as new_file:
            pass

    return 'Created: \n' + "\n".join(app_dirs + app_files)

try:
    script, app_name = sys.argv
    print(struct_app(app_name))
except ValueError:
    print("Usage: %s app_name_here" % sys.argv[0])

