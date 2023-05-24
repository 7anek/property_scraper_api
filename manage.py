#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import socket

def main():
    """Run administrative tasks."""
    # os.system("sudo service postgresql start")#można to zrobić automatycznie przy uruchamianiu windowsa

    ipaddress = socket.gethostbyname(socket.gethostname())
    local = ipaddress == '127.0.1.1' or ipaddress == '192.168.0.46'
    if local:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'properties_scrapping.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'properties_scrapping.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
