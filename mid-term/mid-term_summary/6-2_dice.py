'''
프로그램 이름 : 주사위 3개를 동시에 던져 동일한 숫자 나오기
프로그램 설명 : 세 개의 주사위를 동시에 던져서 그 합이 10이 되는 경우를 찾는다.
'''

import random   #랜덤 모듈을 가져온다.

count = 0                       #시도 횟수를 저장하는 변수를 초기화한다.
dice1, dice2, dice3 = 0, 0, 0   #세 개의 주사위 값을 저장할 변수를 초기화한다.

while True:         #무한 루프를 시작한다.
    count += 1      #시도 횟수를 증가시킨다.
    dice1 = random.randint(1, 6)   #첫 번째 주사위를 던진다.
    dice2 = random.randint(1, 6)   #두 번째 주사위를 던진다.
    dice3 = random.randint(1, 6)   #세 번째 주사위를 던진다.

    #세 주사위의 합이 10이 되는 경우
    if dice1 + dice2 + dice3 == 10:
        #주사위의 값과 시도 횟수를 출력합니다.
        print("dice1 ===> ", dice1)
        print("dice2 ===> ", dice2)
        print("dice3 ===> ", dice3)
        print(count, "번 만에 탈출!")
        break       #무한루프를 빠져나온다.
