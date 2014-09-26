#!/bin/env python
# Directory structure maker for Flask projects.
# Do whatever you want with this.
# - seb
import os, sys

# Few core directories
app_dirs = (
    'app/templates',
    'app/static',
    'app/main',
    'migrations',
    'tests',
    'venv',
)
# Main config files for the project
app_files = (
    'app/main/__init__py',
    'app/main/errors.py',
    'app/main/forms.py',
    'app/main/views.py',
    'app/__init__.py',
    'app/email.py',
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
        new_file = open(os.path.abspath('%s/%s' % (app_name, f)), 'w')
        new_file.close()

try:
    script, app_name = sys.argv
    struct_app(app_name)
except ValueError:
    print("Usage: %s app_name_here" % sys.argv[0])

