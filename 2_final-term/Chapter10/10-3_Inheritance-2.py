'''
일자 : 10주차 보강 (2024.06.14)
범위 : Chapter 10. 객체 지향 프로그래밍
참고 : [Re:Python] 1. self 이해하기 - https://velog.io/@magnoliarfsit/RePython-1.-self-이해하기
'''
### 기말고사 시험 출제 예정 ###
# 속성 입력 : input().split 사용하기

## 클래스 정의부 : 클래스는 새로 만드는 부분
class Rabbit :
    # 속성 : 클래스의 데이터에 해당
    shape = ''
    xPos = 0
    yPos = 0

    # 생성자 정의 : 객체명 = 클래스명()
    def __init__(self, value, x, y) :
        self.shape = value
        self.xPos = x
        self.yPos = y

    # 소멸자 정의 : del(객체명)
    def __del__(self) :
        print("이제 ** %s ** 객체는 소멸됩니다." %(self.shape))

    # 메소드 : 클래스의 기능(함수)에 해당
    def goto(self, x, y) :  # self(default) : 객체(인스턴스) 자기 자신을 참조하는 매개변수
        self.xPos = x
        self.yPos = y

# 상속관계 정의 : ()안에 부모클래스를 명시해준다.
# Rabbit : 부모클래스 / HouseRabbit : 자식클래스
class HouseRabbit(Rabbit) :
    owner = ''
    def eatFeed(self) :
        print("%s가 사료를 먹습니다." %(self.shape))
# Rabbit : 부모클래스 / MountainRabbit : 자식클래스
class MountainRabbit(Rabbit) :
    mountain = ''
    def eatWildglass(self) :
        print("산토끼가 들풀을 먹습니다.")

shape, x, y = input("hRabbit 객체 생성 초기화 : ").split()
x = int(x)
y = int(y)

## 전역변수 정의부
# 객체 생성하는 방법 : 객체명 = 클래스명()
hRabbit = HouseRabbit(shape, x, y)           # 자식클래스 HouseRabbit의 객체 생성
mRabbit = MountainRabbit("산토끼", 300, 400)  # 자식클래스 MountainRabbit의 객체 생성

# 객체의 속성에 접근하는 방법 : 객체명.속성명
#hRabbit.shape = "집토끼"
#mRabbit.shape = "산토끼"

## main 함수부
# 객체의 메서드를 호출하는 방법 : 객체명.메소드(매개변수)
#hRabbit.goto(100, 200)
#mRabbit.goto(300, 400)

print("hRabbit의 모양 :", hRabbit.shape)
print("mRabbit의 모양 :", mRabbit.shape)

print("** 집토끼의 현재 위치는 (%d, %d)" %(hRabbit.xPos, hRabbit.yPos))
print("** 산토끼의 현재 위치는 (%d, %d)" %(mRabbit.xPos, mRabbit.yPos))

# 객체의 메서드를 호출(자식클래스)
hRabbit.eatFeed()
mRabbit.eatWildglass()
