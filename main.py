import os

from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyScientistsLair.settings')
execute_from_command_line('manage.py runserver 127.0.0.1:8000'.split())
#execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())