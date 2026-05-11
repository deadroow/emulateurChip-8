# Constantes pour les couleurs ANSI dans le terminal
ROUGE = "\033[0;31m"    # Erreur
VERT = "\033[0;32m"     # charger Rom /op_Dessin/op_ecran
MARRON = "\033[0;30m"   # op_clavier
BLEU = "\033[0;34m"     # op_saut/stack
VIOLET = "\033[0;35m"   # op_timer/delay
CYAN = "\033[0;36m"     # op_registre_v[x/y]
JAUNE = "\033[1;33m"    # op_registre_I    
NO_COLOR="\033[0m"      #

 


def texte(msg, color="info"): 
    """ Retourne un message coloré pour le terminal. """
    match(color.lower()):
        
        case 'rouge': return f'{ROUGE}{msg}{NO_COLOR}'
        case 'vert': return f'{VERT}{msg}{NO_COLOR}'        
        case 'marron': return f'{MARRON}{msg}{NO_COLOR}'        
        case 'bleu': return f'{BLEU}{msg}{NO_COLOR}'        
        case 'violet': return f'{VIOLET}{msg}{NO_COLOR}'
        case 'cyan': return f'{CYAN}{msg}{NO_COLOR}'
        case 'jaune': return f'{JAUNE}{msg}{NO_COLOR}'

        case _: return f'{msg}' # Pas de couleur par défaut.