import random   #랜덤 모듈을 가져온다.

count = 0                       #시도 횟수를 저장하는 변수를 초기화한다.
dice1, dice2, dice3 = 0, 0, 0   #세 개의 주사위 값을 저장할 변수를 초기화한다.

while True:         #무한 루프를 시작한다.
    count += 1      #시도 횟수를 증가시킨다.
    dice1 = random.randint(1, 6)   #첫 번째 주사위를 던진다.
    dice2 = random.randint(1, 6)   #두 번째 주사위를 던진다.
    dice3 = random.randint(1, 6)   #세 번째 주사위를 던진다.

    #세 주사위의 합이 7이 되는 경우
    if dice1 + dice2 + dice3 == 7:
        #주사위의 값과 시도 횟수를 출력합니다.
        print("주사위 1번: %d, 주사위 2번: %d, 주사위 3번: %d" %(dice1, dice2, dice3))
        print("세 주사위 합이 7이 되었습니다. 주사위를 총 %d번 던졌습니다." %(count))
        break       #무한루프를 빠져나온다.
