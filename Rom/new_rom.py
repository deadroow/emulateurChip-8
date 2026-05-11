import os
from outils.Couleur import texte
from outils.clear import clear_screen


class CreateRom:
    @staticmethod
    def creer(chemin,data:str):
        Dossier_Rom="stockage_Rom"
        if not os.path.exists(Dossier_Rom):
            os.makedirs(Dossier_Rom)
        
        # On combine le dossier et le nom du fichier proprement
        chemin_final = os.path.join(Dossier_Rom, chemin)


        with open(file=chemin_final,mode="wb") as fp:
            binary_data = bytes.fromhex(data)
            fp.write(binary_data)
        print(texte(f"Fichier créé : {chemin_final}", "vert"))


    @staticmethod
    def aide():
        clear_screen()
        guide=texte("----------------------------- \n"
        "Aide pour crée une ROM CHIP8: \n\n"
        "La Commande de création de ROM est la suivante, a éxecuter dans le main:\n" 
        "Dossier_Rom=CreateRom.creer('nom de la rom','suite d'octet')\n\n" 
        "les opcode de la ROM sont découper par octet ex on créer la ROM qui contient les 2 opcode suivant '00E0 1203' on doit l'écrire '00 E0 12 03' \n " 
        "-----------------------------------"\
        ,"jaune")

        print(guide)