'''
프로그램 이름 : 컴퓨터와 인간의 숫자 맞히기 대결
프로그램 설명 : 
'''

import random

computer, user = 0, 0

for i in range(1 , 11, 1) :
    computer = random.randint(1, 5)
    print("[%d회차 게임]" %(i))
    user = int(input("컴퓨터가 생각한 숫자 : "))
    
    if computer == user :
        print("맞혔습니다!\n")
        break
    else :
        print("틀렸습니다.", computer, "였습니다.\n")

print("게임을 마칩니다.")