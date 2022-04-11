# By Luc VINCENT 
# 2022.04.05
# module game
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'


def play(width:int, height:int)->list:
    '''
    width: int la largeur de la grille de jeu
    height: int la hauteur de la grille de jeu
    CU: 4 < width * height < 64
    except : assertionError
    answer : list of int [abcissa, ordinate]
    0 <= abcissa <= width and 0 <= ordinate <= height
    '''
    # précondtions
    assert type(width) is int \
           and type(height) is int, "type argument non respecté"
    assert 4 <= width * height \
           and width * height <= 64, "taille grille non respectée"
    
    answer = [-1, -1]
    while answer[0] == -1:
        try :
            answer[0]  = abs(int(input(f"Entrer l'abcisse, de 0 à {width-1} : ")))
        except ValueError:
            print("Entrer un nombre entier")
        if answer[0] >= width:
            answer[0] = -1
                
    while answer[1] == -1:
        try:
            answer[1]  = abs(int(input(f"Entrer l'ordonnée, de 0 à {height-1} : ")))
        except ValueError:
            print("Entrer un nombre entier")
        if answer[1] >= height:
            answer[1] = -1
    
    
    # postconditions
    assert type(answer) is list, "type renvoyé non conforme"
    assert len(answer) == 2, "Valeur renvoyée invalide"
    
    return answer
    
    

if __name__ == "__main__":
    play(6, 5)