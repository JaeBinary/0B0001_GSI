'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 05. 조건문
'''

import random

myHand = input("Rock(R) / Paper(P) / Scissors(S) : ")

comHand = random.choice(['R', 'P', 'S'])
print("comHand : %c" %(comHand))

if myHand == 'R' :
    if comHand == 'R' :
        print("Draw!")
    elif comHand == 'P' :
        print("Lose!")
    elif comHand == 'S' :
        print("Win!")

if myHand == 'P' :
    if comHand == 'R' :
        print("Win!")
    elif comHand == 'P' :
        print("Draw!")
    elif comHand == 'S' :
        print("Lose!")

if myHand == 'S' :
    if comHand == 'R' :
        print("Draw!")
    elif comHand == 'P' :
        print("Lose!")
    elif comHand == 'S' :
        print("Win!")
