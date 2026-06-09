# Émulateur Chip-8

Ce projet est un **émulateur Chip-8** : un programme qui lis des jeux rétro et les fait
tourner avec Python et Pygame.

Vous choisissez un fichier de jeu (une **ROM** au format
`.ch8`) à travers une interface graphique, et l'émulateur l'exécute : il
lit les instructions du jeu, affiche l'image à l'écran, joue le son et
réagit à votre clavier, exactement comme le ferait la console d'origine.

## Comment ça marche

Au lancement, une fenêtre s'ouvre pour vous laisser sélectionner la ROM que
vous voulez jouer. Une fois le fichier choisi, la fenêtre de jeu démarre et
vous pouvez jouer au clavier.
Le clavier est composé de 16 touches pour reproduire le clavier de l'époque :
1 2 3 4
A Z E R
Q S D F
W X C V

## Installation

L'installation se fait en quelques étapes et **dépend de votre système d'exploitation**. 
Choisissez le guide correspondant au vôtre :

- **Windows** → suivez le guide [Installation sur Windows](#)
- **Linux (Ubuntu / Debian)** → suivez le guide [Installation sur Linux](#)

> [!NOTE]
> Les deux méthodes aboutissent au même résultat, mais les prérequis à
> installer ne sont pas les mêmes selon le système. Suivez bien le guide
> de votre OS, étape par étape, dans l'ordre.

# #émulateur-chip-8--installation-sur-windows

## Étape 1 : Installer Python

Téléchargez Python depuis le site Microsoft :
https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=fr-FR&gl=FR

Cliquez sur "Télécharger".

> [!IMPORTANT]
> Sur le tout premier écran de l'installation, cochez la case
> **"Add Python to PATH"** (en bas de la fenêtre) AVANT de cliquer
> sur « Install Now ».
>
> Si vous oubliez cette case, les commandes `python` ne seront pas
> reconnues et l'installation échouera. En cas d'oubli, désinstallez
> Python et recommencez en cochant la case.

## Étape 2 : Installer Chocolatey

Chocolatey est un gestionnaire de paquets qui nous sert à installer `git` et `make`.

1. Ouvrez **PowerShell en tant qu'administrateur** :
   Clic droit sur le menu Démarrer → **"Windows PowerShell (admin)"**.

2. Collez cette commande et appuyez sur Entrée, cela télécharge Chocolatey (gestionnaire de téléchargement) :
```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

3. Fermez puis rouvrez **PowerShell administrateur** pour
   que Chocolatey soit pris en compte. Vérifiez avec :
```choco --version```

## Étape 3 : Installer Git et Make

Toujours dans **PowerShell administrateur**, tapez :
```choco install git -y```
```choco install make -y```

> Git installe aussi **"Git Bash"**, le terminal dont vous aurez besoin
> à l'étape suivante. Make permet de lancer l'installation et le programme.

Une fois terminé, **fermez PowerShell**.

## Étape 4 : Récupérer le projet

1. Ouvrez **Git Bash** (cherchez "Git Bash" dans le menu Démarrer).

   > Utilisez bien **Git Bash**, et non PowerShell, pour toutes les
   > commandes qui suivent. PowerShell ne sait pas exécuter le script
   > d'installation et provoquerait une erreur.

2. Placez-vous où vous voulez télécharger le projet, par exemple le bureau :
```cd ~/Desktop```

3. Clonez le dépôt dans ce dossier :
```git clone https://github.com/deadroow/emulateurChip-8.git```

4. Entrez dans le dossier du projet :
```cd emulateurChip-8```

## Étape 5 : Installer les dépendances

Toujours dans **Git Bash**, dans le dossier du projet :
```make install```

Cette commande crée un environnement Python isolé (`.venv`) et installe
toutes les bibliothèques nécessaires (Gooey, pygame, etc.).
Patientez car l'installation peut prendre quelques minutes.

## Étape 6 : Lancer le programme
```make run```

Une fenêtre s'ouvre pour choisir un fichier ROM (`.ch8`), puis l'émulateur
démarre.

## Relancer le programme plus tard

L'environnement reste installé. Pour rejouer un autre jour :

1. Ouvrez **Git Bash**.
2. Replacez-vous dans le dossier du projet :
```cd ~/Desktop/emulateurChip-8```
   (adaptez le chemin (/Desktop) si vous l'avez mis ailleurs)
3. Lancez :
```make run```

Pas besoin de refaire `make install` : il ne sert qu'à la première
installation.

## En cas de problème

**"python n'est pas reconnu…" ou erreur sur Python pendant `make install`"**
→ Python n'a pas été ajouté au PATH. Désinstallez Python, réinstallez-le
en cochant **"Add Python to PATH"** (Étape 1), puis fermez et rouvrez
Git Bash.

**"make : command not found" ou "choco : terme non reconnu"**
→ Fermez et rouvrez le terminal après les installations. Si l'erreur
persiste, c'est que l'étape correspondante (Chocolatey, git ou make)
n'a pas réussi : reprenez-la dans PowerShell administrateur.

**Erreur "CreateProcess(... bash ...) failed" au moment de `make install`"**
→ Vous lancez `make` depuis PowerShell. Utilisez **Git Bash** à la place
(Étape 4).

**"No module named 'gooey'" (ou un autre module) au lancement"**
→ Les dépendances ne se sont pas installées correctement. Dans Git Bash,
dans le dossier du projet, relancez :
make install


# #émulateur-chip-8--installation-sur-linux

> [!NOTE]
> Ce guide est écrit pour Ubuntu et Debian (commande `apt`). Pour Fedora,
> Arch ou une autre distribution, le principe est identique mais le nom du
> gestionnaire de paquets et des bibliothèques change.

## Étape 1 : Installer les prérequis système

Sous Linux, `make`, `git` et `bash` peuvent être installés directement
depuis le terminal. Python a aussi besoin de quelques bibliothèques
système pour que l'interface graphique (Gooey/wxPython) fonctionne.

Ouvrez un terminal (CTRL+Alt+T) et tapez :
```sudo apt update```
```sudo apt install -y python3 python3-venv python3-dev python3-pip build-essential libgtk-3-dev make git Libgtk-3-dev libsdl2-2.0-0 libsdl2-dev libglu1-mesa Libglu1-mesa-dev Libjpeg-dev libtiff-dev libpng-dev```

> [!IMPORTANT]
> Cette commande demande votre **mot de passe** (celui de votre session).
> C'est normal : `sudo` exécute l'installation avec les droits
> administrateur. Le mot de passe ne s'affiche pas à l'écran pendant que
> vous le tapez, c'est voulu.
>
> Les paquets `python3-venv`, `build-essential` et `libgtk-3-dev` sont
> indispensables : sans eux, l'installation des dépendances échouera

## Étape 2 : Récupérer le projet

1. Placez-vous où vous voulez télécharger le projet, par exemple votre
   dossier personnel :
```cd ~```

2. Clonez le dépôt dans ce dossier :
```git clone https://github.com/deadroow/emulateurChip-8.git```

3. Entrez dans le dossier du projet :
```cd emulateurChip-8```

## Étape 3 : Installer les dépendances

Dans le dossier du projet, tapez :
```chmod 777 init.sh```
Puis :
```make install```

Cette commande crée un environnement Python isolé (`.venv`) et installe
toutes les bibliothèques nécessaires (Gooey, pygame, etc.).
Patientez car l'installation peut prendre quelques minutes.

## Étape 4 : Lancer le programme
make run

Une fenêtre s'ouvre pour choisir un fichier ROM (`.ch8`), puis l'émulateur
démarre.

## Relancer le programme plus tard

L'environnement reste installé. Pour rejouer un autre jour :

1. Ouvrez un terminal.
2. Replacez-vous dans le dossier du projet :
cd ~/emulateurChip-8
   (adaptez le chemin si vous l'avez mis ailleurs)
3. Lancez :
make run

Pas besoin de refaire `make install` : il ne sert qu'à la première
installation.

## En cas de problème

**"ImportError: libSDL2-2.0.so.0: cannot open shared object file"**
→ installez SDL2 :
```sudo apt update```
```sudo apt install -y libsdl2-2.0-0 libsdl2-dev```
puis vérifiez que l'installation à bien marché :
```ldconfig -p | grep SDL2```
vous devez obtenir une ligne ressembl
```libSDL2-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0```

**"make: command not found"**
→ `make` n'est pas installé. Reprenez l'Étape 1 :
```sudo apt install -y make```.

**"The virtual environment was not created…" ou erreur sur `venv`**
→ Le paquet `python3-venv` manque. Tapez `sudo apt install -y python3-venv`,
puis relancez `make install`.

**"No module named 'gooey'" (ou un autre module) au lancement**
→ Les dépendances ne se sont pas installées correctement, le plus souvent
parce que **wxPython** n'a pas pu se compiler. Vérifiez d'abord que les
bibliothèques système sont présentes :
sudo apt install -y python3-dev build-essential libgtk-3-dev
Puis relancez `make install`.

Si l'erreur persiste, installez wxPython depuis une version précompilée
(remplacez `ubuntu-24.04` par votre version, visible avec `lsb_release -rs`) :
.venv/bin/python -m pip install -U 
-f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04 
wxPython
Puis à nouveau `make install`.

**La fenêtre graphique ne s'ouvre pas / erreur "no display"**
→ Vous êtes probablement sur un serveur sans interface graphique, ou via
SSH sans redirection d'affichage. L'émulateur a besoin d'un bureau
graphique pour afficher Gooey et la fenêtre de jeu.