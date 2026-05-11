Étape 1 : Prérequis
Linux : make est généralement déjà installé. Sinon : sudo apt install build-essential.

Windows : Vous devez avoir make. Si vous avez Chocolatey, lancez un terminal en administrateur et tapez :
  choco install make



Étape 2 : Clonage et Initialisation
Ouvrez un terminal (Bash recommandé) et exécutez les commandes suivantes :

# 1. Cloner le dépôt et se déplacer dessus.
git clone git@github.com:deadroow/emulateurChip-8
cd emulateurChip-8

# 2. Préparer l'environnement (crée le .venv et installe les dépendances)
make menu

# 3. Activer l'environnement (.venv)
Windows : source .venv/Scripts/activates
Linux : source .venv/bin/activate

# 4. Lancer le programme
make run     
