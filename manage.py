#!/usr/bin/env python
import os
import sys

def main():
    # Ici on dit à Django que tes configurations sont dans le dossier project_config
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Est-ce qu'il est bien installé ? "
            "As-tu pensé à activer ton environnement virtuel (.venv) ?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()