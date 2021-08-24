##
## EPITECH PROJECT, 2021
## Pendu
## File description:
## pendu
##

import random

def pendu():
    list_of_words = ["patate", "lait", "kinder", "delice", "chocolat", \
                    "cuticule", "arbre", "mouette", "caviar", "truffe", "immeuble", \
                    "bouder", "moustache", ]
    word_to_find = list_of_words[random.randint(0, len(list_of_words))]
    size = len(word_to_find)
    underscore = ["_"]
    underscore = underscore*size
    score = size
    life = 11

    while life != 0 and score != 0:
        choose_a_letter = input("choose a letter ")
        print('\n')
        if choose_a_letter in word_to_find:
            position=int(word_to_find.index(choose_a_letter))
            underscore.pop(position)
            underscore.insert(position,choose_a_letter)
            result = ' '.join(underscore)
            print(result)
            score -= 1
        else:
            print ("Too bad\n")
            if score == size:
                print(size*"_")
            else:
                print(result)
                life -= 1
                print("life remaining : " + life + '\n')
        if life == 0:
            print("you lose !\n")
        elif score == 0:
            print("You win !\n")
            break

pendu()