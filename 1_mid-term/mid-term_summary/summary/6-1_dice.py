'''
일자 : 6주차 (2024.04.12)
범위 : Chapter 06. 반복문
'''
#중간고사 출제 가능성
import random # 모듈 가져오기

count = 0
dice1, dice2, dice3 = 0, 0, 0


while 1 :   # 1 == True
    count += 1
    dice1 = random.randint(1, 6) #모듈.함수()
    dice2 = random.randint(1, 6) #모듈.함수()
    dice3 = random.randint(1, 6) #모듈.함수()

    if(dice1 + dice2 + dice3 == 10) :
        print("dice1 : %d\ndice2 : %d\ndice3 : %d\n%d번만에 탈출" %(dice1, dice2, dice3, count))
        break
