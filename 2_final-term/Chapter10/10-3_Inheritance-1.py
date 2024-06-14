'''
일자 : 14주차 (2024.06.07)
범위 : Chapter 10. 객체 지향 프로그래밍
참고 : [Re:Python] 1. self 이해하기 - https://velog.io/@magnoliarfsit/RePython-1.-self-이해하기
'''
### 기말고사 시험 출제 예정(다음주에 이어서) ###

## 클래스 정의부 : 클래스는 새로 만드는 부분
class Rabbit :
    # 속성 : 클래스의 데이터에 해당
    shape = ''
    xPos = 0
    yPos = 0

    # 생성자 정의
    def __init__(self, value) :
        self.shape = value

    # 소멸자 정의
    def __del__(self) :
        print("이제 ** %s ** 객체는 소멸됩니다." %(self.shape))

    # 메소드 : 클래스의 기능(함수)에 해당
    def goto(self, x, y) :  # self(default) : 객체(인스턴스) 자기 자신을 참조하는 매개변수
        self.xPos = x
        self.yPos = y
    '''
    def print_pos(self, x, y) :
        print("** 토끼의 현재 위치는 (%d, %d)" %(x, y))
    '''

# 상속관계 정의 : ()안에 부모클래스를 명시해준다.
# Rabbit : 부모클래스 / HouseRabbit : 자식클래스
class HouseRabbit(Rabbit) :
    owner = ''
    def eatFeed(self) :
        print("집토끼가 사료를 먹습니다.")
# Rabbit : 부모클래스 / MountainRabbit : 자식클래스
class MountainRabbit(Rabbit) :
    mountain = ''
    def eatWildglass(self) :
        print("산토끼가 들풀을 먹습니다.")

## 전역변수 정의부
hRabbit = HouseRabbit("집토끼")     # 자식클래스 HouseRabbit의 객체 생성
mRabbit = MountainRabbit("산토끼")  # 자식클래스 MountainRabbit의 객체 생성

## main 함수부
hRabbit.goto(100, 200)
mRabbit.goto(300, 400)

print("hRabbit의 모양 :", hRabbit.shape)
print("mRabbit의 모양 :", mRabbit.shape)

print("** 집토끼의 현재 위치는 (%d, %d)" %(hRabbit.xPos, hRabbit.yPos))
print("** 산토끼의 현재 위치는 (%d, %d)" %(hRabbit.xPos, hRabbit.yPos))

hRabbit.eatFeed()
mRabbit.eatWildglass()
