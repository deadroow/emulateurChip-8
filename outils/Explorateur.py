from gooey import Gooey, GooeyParser
import subprocess
import sys
import os

# Petit script Gooey qui sert a choisir une ROM Chip-8.
# Gooey transforme le code en une interface graphique pour être user-friendly
@Gooey(
    program_name="Emulateur Chip8 - Launcher",
    program_description="Sélectionnez un fichier ROM .ch8 pour lancer l'émulation",
    progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
    progress_expr="current / total * 100"
)

def chemin():
    # Parser Gooey pour gérer les arguments utilisateur
    parser = GooeyParser(description="Sélectionnez le fichier Chip8 que vous voulez exécuter")

    # Argument qui force la sélection seulement aux fichiers .ch8 via l'explorateur de fichiers
    parser.add_argument(
        'Filename',
        help="Fichier .ch8",
        widget='FileChooser',
        gooey_options=dict(wildcard="Fichier Chip8 (*.ch8)|*.ch8")
    )

    # Récupère les arguments fournis par l'utilisateur via l'interface
    args = parser.parse_args()

    # Stocke le chemin du fichier sélectionné
    fichier = args.Filename

    # Vérifie que le fichier existe
    if not os.path.isfile(fichier):
        print(f"Erreur : le fichier '{fichier}' n'existe pas.")
        sys.exit(1)
    print(f"Fichier sélectionné : {fichier}")

    # Remonte d'un dossier pour atteindre la racine du projet où se trouve main.py (car Explorateur.py est dans /outils)
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    emulator_path = os.path.join(racine, "main.py")

    # Vérifie que main.py existe
    if not os.path.isfile(emulator_path):
        print(f"Erreur : main.py introuvable à '{emulator_path}'")
        sys.exit(1)
        
    print("Lancement de l'emulateur")
    try:
        subprocess.run(
            [sys.executable, emulator_path, fichier],
            check=True,
            cwd=racine
        )
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'execution de l'emulateur : {e}")

def main():
    chemin()

# Pour lancer le programme
if __name__=="__main__":
    main()