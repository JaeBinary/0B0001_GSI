'''
프로그램 이름 : 주사위 3개를 동시에 던져 동일한 숫자 나오기
프로그램 설명 : 
'''

import random   #모듈 가져오기

count = 0
dice1, dice2, dice3 = 0, 0, 0


while 1 :   #1 == True
    count += 1
    dice1 = random.randint(1, 6) #모듈.함수(이상, 이하) : 이상 값 ~ 이하 값
    dice2 = random.randint(1, 6) #모듈.함수(이상, 이하) : 이상 값 ~ 이하 값
    dice3 = random.randint(1, 6) #모듈.함수(이상, 이하) : 이상 값 ~ 이하 값

    if(dice1 + dice2 + dice3 == 10) :
        print("dice1 : %d\ndice2 : %d\ndice3 : %d\n%d번만에 탈출" %(dice1, dice2, dice3, count))
        break