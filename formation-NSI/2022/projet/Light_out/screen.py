# By Luc VINCENT 
# 2022.04.05
# module screen
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

def display(board:list):
    '''
    afficher la grille de jeu à l'écran
    board: une grille
    CU: 4 à 64 cases des 0 ou des 1
    
    '''
    # précondtions
    assert type(board) is list, " Erreur type argument"
    assert len(board) >= 1, "Grille incohérente"
    row = len(board)
    assert type(board[0]) is list, " Erreur type argument"
    column = len(board[0])
    for i in range(row):
        assert column == len(board[i]), "Grille incohérente"
    assert 0 <=   row *   column <= 64 ,"Grille non conforme"
    
    for i in range(row):
        for j in range(column):
            print(board[i][j], end=' ')
        print()
    

if __name__ == "__main__":
    # exemple de test
    display([[1, 1, 1], [0, 0, 0]])