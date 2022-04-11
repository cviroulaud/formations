# By Luc VINCENT 
# 2022.04.05
# module light_out
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'



# Définir les contraintes
BOX_MIN = 4
BOX_MAX = 64
MAX_TRIALS = 100

from init import initialise
from game import play
from compute import evolution, somme
from screen import display

# intialiser le jeu
[width, height, trials_max] = initialise(MAX_TRIALS, BOX_MAX, BOX_MIN)
# On va jouer
playing = True
# On a pas encore essayé
trials = 0

# créeer la structure du plateau de jeu
board =[[1 for i in range(width)] for j in range(height)]

# afficher la grille
display(board)

# boucle de jeu
while playing and trials <= trials_max:
    [x, y] = play(width, height)
    evolution([x, y], board)
    display(board)
    trials += 1
    playing = somme(board)
    
# message de fin
if not playing:
    print(f"vous avez réussi après {trials} essais")
else:
    print(f"vous avez échoué après {trials} essais")



