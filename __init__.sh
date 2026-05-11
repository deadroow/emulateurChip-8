#!/bin/bash

set -euo pipefail

create_venv_boilerplate(){
    echo "________________"
    if [ ! -d ".venv" ]; then
        py -m venv .venv
        
        source .venv/Scripts/activate
        if [ ! -f "requirements.txt" ]; then
            pip install pylint pygame pytest
            pip freeze > requirements.txt
        else
            echo "[create_venv_bp] requirements.txt already exists"
            pip install -r requirements.txt
        fi
    else
        echo "[create_venv_bp] .venv already exists"
    fi
    echo "________________"
}

create_venv_boilerplate