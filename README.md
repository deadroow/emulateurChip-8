# Émulateur Chip-8 - Installation sur Windows

## Étape 1 : Installer Python

Téléchargez Python depuis le site officiel :
https://www.python.org/downloads/

Télécharger la dernière version pour Windows de l'installateur.

> **TRÈS IMPORTANT** : sur le tout premier écran de l'installation,
> cochez la case **"Add Python to PATH"** (en bas de la fenêtre)
> AVANT de cliquer sur « Install Now ».
>
> Si vous oubliez cette case, les commandes `python` ne seront pas
> reconnues et l'installation échouera plus loin. En cas d'oubli,
> désinstallez Python et recommencez en cochant la case.

## Étape 2 : Installer Chocolatey

Chocolatey est un gestionnaire de paquets qui nous sert à installer `git` et `make`.

1. Ouvrez **PowerShell en tant qu'administrateur** :
   Clic droit sur le menu Démarrer → **"Windows PowerShell (admin)"**.

2. Collez cette commande et appuyez sur Entrée, cela télécharge Chocolatey (gestionnaire de téléchargement) :
Set-ExecutionPolicy Bypass -Scope Process -Force;    [System.Net.ServicePointManager]::SecurityProtocol =
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

3. Fermez puis rouvrez **PowerShell administrateur** pour
   que Chocolatey soit pris en compte. Vérifiez avec :
choco --version

## Étape 3 : Installer Git et Make

Toujours dans **PowerShell administrateur**, tapez :
choco install git -y
choco install make -y

> Git installe aussi **"Git Bash"**, le terminal dont vous aurez besoin
> à l'étape suivante. Make permet de lancer l'installation et le programme.

Une fois terminé, **fermez PowerShell**.

## Étape 4 : Récupérer le projet

1. Ouvrez **Git Bash** (cherchez "Git Bash" dans le menu Démarrer).

   > Utilisez bien **Git Bash**, et non PowerShell, pour toutes les
   > commandes qui suivent. PowerShell ne sait pas exécuter le script
   > d'installation et provoquerait une erreur.

2. Placez-vous où vous voulez télécharger le projet, par exemple le bureau :
cd ~/Desktop

3. Clonez le dépôt dans ce dossier :
git clone https://github.com/deadroow/emulateurChip-8.git

4. Entrez dans le dossier du projet :
cd emulateurChip-8

## Étape 5 : Installer les dépendances

Toujours dans **Git Bash**, dans le dossier du projet :
make install

Cette commande crée un environnement Python isolé (`.venv`) et installe
toutes les bibliothèques nécessaires (Gooey, pygame, etc.).
Patientez car l'installation peut prendre quelques minutes.

## Étape 6 : Lancer le programme
make run

Une fenêtre s'ouvre pour choisir un fichier ROM (`.ch8`), puis l'émulateur
démarre.

## Relancer le programme plus tard

L'environnement reste installé. Pour rejouer un autre jour :

1. Ouvrez **Git Bash**.
2. Replacez-vous dans le dossier du projet :
cd ~/Desktop/emulateurChip-8
   (adaptez le chemin (/Desktop) si vous l'avez mis ailleurs)
3. Lancez :
make run

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
