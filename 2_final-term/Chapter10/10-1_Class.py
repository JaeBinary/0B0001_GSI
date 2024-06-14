'''
일자 : 14주차 (2024.06.07)
범위 : Chapter 10. 객체 지향 프로그래밍
참고 : [Re:Python] 1. self 이해하기 - https://velog.io/@magnoliarfsit/RePython-1.-self-이해하기
'''

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

## 전역변수 정의부
rabbit = None   # 객체변수로 사용한 변수 생성
userX, userY = 0, 0

## main 함수부
# Rabbit클래스의 rabbit 객체 생성
# Rabbit() : 생성자 __init__(self)메소드가 자동 호출
rabbit = Rabbit("산토끼")
#rabbit.shape = "토끼"

print("rabbit의 모양 :", rabbit.shape) # 생성자로 초기화된 shape 속성 값을 출력

while True :
    userX = int(input("토끼가 이동할 X좌표 ==> "))
    userY = int(input("토끼가 이동할 Y좌표 ==> "))

    rabbit.goto(userX, userY) # 메소드 호출
    '''
    rabbit.print_pos(userX, userY)
    '''
    print("** 토끼의 현재 위치는 (%d, %d)" %(rabbit.xPos, rabbit.yPos))

    if userX == 0 :
        del(rabbit) # rabbit 객체를 제거함. 즉, 소멸자 자동 호출
        break
