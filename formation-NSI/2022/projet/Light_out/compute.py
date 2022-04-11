# By Luc VINCENT 
# 2022.04.05
# module compute
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'



def somme(board:list)->bool:
    '''
    renvoyer faux si la somme de la grille est nulle
    '''
    somme = 0
    for ligne in board:
        for val in ligne:
            somme += val
    if somme == 0:
        return False
    else:
        return True




def delta(target:int, edge:int)->tuple:
    '''
    renvoyer la variation possible de target pour trouver
    les voisins possibles en x ou y
    renvoie un tupe de la plage possible
    '''
    #préconditions
    assert type(target) is int\
           and type(edge) is int, "Errreur de type argument"
    assert 0 <= target \
           and target <= edge, "target hors limite edge"
    
    answer = (0, 0)
    if target == 0:
        answer = (0, 1)
    elif target == edge:
        answer = (edge-1, edge)
    else:
        answer = (target-1, target +1)
    
    # post conditions
    assert type(answer) is tuple, "Erreur type renvoyé"
    return answer

def evolution(position:list, board:list):
    '''
    postion:list[int, int] la position jouée abcisse, ordonnée
    board: list [[], []] la platine de jeu
    modifie board en place
    '''
    
    # préconditions
    assert type(position) is list\
           and type(board) is list, "Erreur de type sur argument position ou board"
    assert len(position) == 2, "Position sur deux valeurs"
    assert type(position[0]) is int \
           and type(position[1]) is int, "abcisse et ordonnées sur deux entiers"
    
    assert len(board) >= 1, "Grille incohérente"
    row = len(board)
    assert type(board[0]) is list, " Erreur type argument"
    column = len(board[0])
    for i in range(row):
        assert type(board[i]) is list, "Erreur de type sur argument board"
        assert len(board[i]) == column, "Grille incohérente"
    
    assert position[1] < len(board)\
           and position[0] < len(board[0]), "Postion hors grille"
    
    
    
    
    # On calcule les cases adjacentes
    delta_x = delta(position[0], len(board[0])-1)
    delta_y = delta(position[1], len(board)-1)
    
    #on modifie les cases
    for x in range(delta_x[0], delta_x[1]+1):
        board[position[1]][x] = (board[position[1]][x] + 1) % 2
    
    for y in range(delta_y[0], delta_y[1]+1):
        board[y][position[0]] = (board[y][position[0]] + 1) % 2   
    
    board[position[1]][position[0]] = (board[position[1]][position[0]] + 1) % 2
        
        

if __name__ == "__main__":
    # exmple de test
    board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    evolution([2,3], board)
    print(board)
    