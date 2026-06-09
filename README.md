## Étape 1 : Prérequis

**Linux** : `make` est généralement déjà installé. Sinon : `sudo apt install build-essential`.

**Windows** : Vous devez avoir `make`. Avec Chocolatey, dans un terminal administrateur :
    choco install make

## Étape 2 : Clonage et Initialisation

Ouvrez un terminal et exécutez :

    # 1. Cloner le dépôt et s'y déplacer
    git clone git@github.com:deadroow/emulateurChip-8
    cd emulateurChip-8

    # 2. Préparer l'environnement (crée le .venv et installe les dépendances)
    make install

    # 3. Lancer le programme
    make run

## Relancer le programme plus tard

Une fois l'installation faite (Étape 2), le `.venv` et les dépendances
restent en place. Pour relancer le programme un autre jour, il suffit de faire dans le terminal :

    cd emulateurChip-8
    make run

Pas besoin de refaire `make install`.
