# By Luc VINCENT 
# 2022.04.05
# module init
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

def initialise(MAX_TRIALS:int, BOX_MAX:int, BOX_MIN:int)->list:
    '''
    MAX_TRIALS: int  Nombre d'essais maxi acceptable
    BOX_MAX : int Nombre maxi de case
    BOX_MIN : int Nombre mini de case
    CU : Valeurs limite arguments 100, 64, 4"
    except : assertionError
    answer : list of int [width, heigth, trials]
    '''
    # préconditions
    assert type(MAX_TRIALS) is int \
           and type(BOX_MAX) \
           and type(BOX_MIN), "Argument entiers SVP"
    assert MAX_TRIALS <= 100 \
           and BOX_MAX <= 64 \
           and BOX_MIN >= 4, "Valeurs limite arguments 100, 64, 4"
    
    # traitement
    answer = [0, 0, 0]
    
    while answer[2] == 0:
        while answer[0] == 0 :
            try :
                answer[0]  = abs(int(input("Entrer la largeur de la grille : ")))
            except ValueError:
                print("Entrer un nombre entier")
        
        while answer[1] == 0 :
            try :
                answer[1] = abs(int(input("Entrer la hauteur de la grille : ")))
            except ValueError:
                print("Entrer un nombre entier")
        # Controle grille
        if BOX_MIN <= (answer[0] * answer[1]) <= BOX_MAX :
            answer[2] = -1
        else:
            print(f"Votre choix de largeur {answer[0]} x hauteur {answer[1]} ne convient pas")
            print(f"{answer[0]*answer[1]} n'est pas compris entre {BOX_MIN} et {BOX_MAX}")
            answer = [0, 0, 0]
    while answer[2] == -1 :
            try :
                answer[2]  = abs(int(input("Entrer le nombre d'essais : ")))
            except ValueError:
                print("Entrer un nombre entier")
            if answer[2] > MAX_TRIALS:
                print(f"Votre choix {answer[2]} n'est pas inférieur à {MAX_TRIALS}")
                answer[2] = -1
       
    # post conditions
    assert type(answer) is list, "type renvoyé non conforme"
    assert len(answer)== 3, "type renvoyé non conforme"
    for i in range(3):
        assert type(answer[i]) is int, "type renvoyé non conforme"
    
    return answer

if __name__ == "__main__":
    # exemple de test
    initialise(100, 64, 4)