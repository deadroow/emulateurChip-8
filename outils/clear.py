import os
def clear_screen(): 
    """ Efface le contenu du terminal selon le système d'exploitation. """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')