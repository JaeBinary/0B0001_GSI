'''코드 10-6 p.326'''
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

## 전역변수 정의부
# 사용자로부터 입력받기
hRabbit_info = input("집토끼의 모양, x 위치, y 위치를 입력하세요 (공백으로 구분): ").split()    # type(hRabbit_info) : list
mRabbit_info = input("산토끼의 모양, x 위치, y 위치를 입력하세요 (공백으로 구분): ").split()    # type(mRabbit_info) : list

# 입력값을 사용하여 객체 생성
hRabbit = HouseRabbit(hRabbit_info[0], int(hRabbit_info[1]), int(hRabbit_info[2]))
mRabbit = MountainRabbit(mRabbit_info[0], int(mRabbit_info[1]), int(mRabbit_info[2]))

## main 함수부
print("hRabbit의 모양 :", hRabbit.shape)
print("mRabbit의 모양 :", mRabbit.shape)

print("** 집토끼의 현재 위치는 (%d, %d)" %(hRabbit.xPos, hRabbit.yPos))
print("** 산토끼의 현재 위치는 (%d, %d)" %(mRabbit.xPos, mRabbit.yPos))

# 객체의 메서드를 호출(자식클래스)
hRabbit.eatFeed()
mRabbit.eatWildglass()
