import pygame
from app import Ecran, chip_8, DetectionTouche
from Rom import ROM, CreateRom
from outils import clear_screen, Explorateur
import subprocess
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RESOLUTIONS = {
    "moyen": (1024, 512),
    "grand": (1280, 640),
}

def main():
    # Dossier ou se trouve main.py, la racine du projet
    DOSSIER_PROJET = os.path.dirname(os.path.abspath(__file__))

    # Si aucun argument n'est fourni, on lance le menu
    if len(sys.argv) < 2:
        chemin_menu = os.path.join(DOSSIER_PROJET, "outils", "Explorateur.py")
        if os.path.exists(chemin_menu):
            subprocess.run([sys.executable, chemin_menu])
        else:
            print(f"Erreur : Le fichier Explorateur est introuvable ici : {chemin_menu}")
        sys.exit(0)

    chemin_rom       = sys.argv[1] # Le chemin de la ROM est dans l'argument 1 (ex : main.py "C:\chemin")
    choix_taille     = sys.argv[2] if len(sys.argv) > 2 else "petit" #  # La taille s'il y en a une (ex : main.py C:\chemin "grand")

    # .get cherche dans le dico RESOLUTIONS la clé correspondante à grand ou moyen, et renvoyer la valeur, sinon c'est (1024, 512) défaut
    largeur, hauteur = RESOLUTIONS.get(choix_taille, (1024, 512)) 

    pygame.init()
    pygame.mixer.init()
    clear_screen()

    # Chemin absolu vers le son, marche peu importe d'ou est lance main.py
    bip = pygame.mixer.Sound(os.path.join(DOSSIER_PROJET, "outils", "bip.wav"))
    son = None
    ecran      = Ecran(largeur_fenetre=largeur, hauteur_fenetre=hauteur)
    clavier    = DetectionTouche()
    cpu        = chip_8(clavier=clavier)
    rom_loader = ROM()

    # Chargment de la Rom dans la mémoire
    try:
        # .__func__ car load est décoré
        rom_loader.load.__func__(cpu, path=chemin_rom)
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        sys.exit(1)


    horloge  = pygame.time.Clock()
    en_cours = True
    

    while en_cours:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            clavier.mise_a_jour(event)

        # mais à jour l'état des touche dans cpu
        cpu.etat_touche = [clavier.est_enfoncee(i) for i in range(16)]

        for _ in range(10): # 600 instruction par second
            cpu.cycle()

        if cpu.delay_timer > 0:
            cpu.delay_timer -= 1

        if cpu.sound_timer > 0:
            if not son or not son.get_busy():
                son = bip.play(loops=-1)
            cpu.sound_timer -= 1

        else:
            if son:
                son.stop()
                son=None

        # rendu graphique
        ecran.display_buffer = cpu.ecran[:]
        ecran.render()

        # régle a 60 par second
        horloge.tick(60)

    ecran.quit()

if __name__ == "__main__":
    main()