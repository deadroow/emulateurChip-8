#!/bin/bash

# Arrête le script en cas d'erreur
set -euo pipefail

create_venv_boilerplate(){
    echo "________________________________________________"
    echo "Instalation des bibliothèque nécéssaire au programme"
    
    # 1. Création du venv s'il n'existe pas
    if [ ! -d ".venv" ]; then
        echo "[init] Création du venv..."
        # On teste 'python' ou 'py' selon le système
        python3 -m venv .venv || python -m venv .venv || py -m venv .venv
    else
        echo "[init] .venv existe déjà."
    fi

    # 2. Détection du script d'activation (Windows vs Linux/Mac)
    if [ -f ".venv/Scripts/activate" ]; then
        source .venv/Scripts/activate
    else
        source .venv/bin/activate
    fi

    # 3. Mise à jour de pip (toujours une bonne pratique)
    pip install --upgrade pip

    # 4. Installation des dépendances
    if [ -f "requirements.txt" ]; then
        echo "[init] Installation des dépendances depuis requirements.txt..."
        pip install -r requirements.txt
    else
        echo "[init] requirements.txt introuvable. Installation par défaut..."
        pip install pylint pygame pytest
        pip freeze > requirements.txt
    fi

    echo "________________________________________________"
    echo "Installation finie."
    echo "Pour bien commencer, il est conseillé d'activer le venv avec : source .venv/Scripts/activate (ou .venv/bin/activate)"
}

create_venv_boilerplate