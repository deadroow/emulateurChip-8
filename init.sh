#!/bin/bash
# Arrête le script en cas d'erreur (sauf là où on gère explicitement l'échec)
set -euo pipefail

create_venv_boilerplate(){
    echo "________________________________________________"
    echo "Installation des bibliothèques nécessaires au programme"

    # Création du venv s'il existe pas (priorité à Python 3.12)
    if [ ! -d ".venv" ]; then
        echo "[init] Création du venv..."
        py -3.12 -m venv .venv 2>/dev/null \
            || python3.12 -m venv .venv 2>/dev/null \
            || python3 -m venv .venv \
            || python -m venv .venv \
            || py -m venv .venv
    else
        echo "[init] .venv existe déjà."
    fi

    # Détection du Python du venv (Windows vs Linux/Mac)
    if [ -f ".venv/Scripts/python.exe" ]; then
        VENV_PY=".venv/Scripts/python.exe"
    elif [ -f ".venv/Scripts/python" ]; then
        VENV_PY=".venv/Scripts/python"
    else
        VENV_PY=".venv/bin/python"
    fi

    # Mise à jour de pip via le Python du venv (pas besoin d'activer)
    "$VENV_PY" -m pip install --upgrade pip || echo "[init] Avertissement : échec mise à jour de pip."

    # Installation des dépendances
    if [ -f "requirements.txt" ]; then
        echo "[init] Installation des dépendances depuis requirements.txt..."
        "$VENV_PY" -m pip install -r requirements.txt \
            || echo "[init] Avertissement : certaines dépendances ont échoué (vérifie wxPython sous Linux)."
    else
        echo "[init] requirements.txt introuvable. Installation par défaut..."
        "$VENV_PY" -m pip install pylint pygame pytest \
            || echo "[init] Avertissement : installation par défaut partielle."
        "$VENV_PY" -m pip freeze > requirements.txt
    fi

    echo "________________________________________________"
    echo "Installation finie."
    echo "Vous pouvez maintenant lancer l'émulateur avec : make run"
}

create_venv_boilerplate