#!/usr/bin/env python3
"""
Point d'entrée de School Helper (application de bureau).

Usage normal :  python run_app.py
Usage packagé : c'est ce fichier que PyInstaller compile en .exe
"""

from gui.app import main

if __name__ == "__main__":
    main()
