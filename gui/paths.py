"""
Résolution des chemins de données, compatible :
- exécution normale (`python -m gui.app`)
- exécutable PyInstaller en mode --onefile (les données doivent vivre à côté
  de l'.exe, pas dans le dossier temporaire _MEIPASS où le code est extrait)
"""

import sys
from pathlib import Path


def get_app_base_dir() -> Path:
    """
    Retourne le dossier où les données persistantes (JSON, SQLite) doivent
    être lues/écrites :
    - si l'app tourne comme .exe PyInstaller : le dossier contenant l'.exe
    - sinon : la racine du projet (parent de gui/)
    """
    if getattr(sys, "frozen", False):
        # PyInstaller : sys.executable pointe vers school_helper.exe
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent
