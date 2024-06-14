'''
일자 : 14주차 (2024.06.07)
범위 : Chapter 10. 객체 지향 프로그래밍
'''

## 클래스 선언
class Line :
    length = 0

    def __init__(self, length) :
        self.length = length
        print(self.length, "길이의 선이 생성되었습니다.")

    def __del__(self) :
        print(self.length, "길이의 선이 제거되었습니다.")

    def __add__(self, other) :
        return self.length + other.length

    def __lt__(self, other) :
        return self.length < other.length

    def __eq__(self, other) :
        return self.length == other.length

## 메인 코드 부분
line1 = Line(10)
line2 = Line(5)

print("두 선의 합 :", line1 + line2)    # __add__() 자동 호출

if line1 < line2 :              # __lt__() 자동 호출
    print("line2가 더 깁니다.")
elif line1 == line2 :           # __eq__() 자동 호출
    print("두 선의 길이가 같습니다.")
else :
    print("line1이 더 깁니다.")
    del(line2)

'''
print("두 선의 합 : ", line1.__add__(line2))

if line1.__lt__(line2) :
    print("line2가 더 깁니다.")
elif line1.__eq__(line2) :
    print("두 선의 길이가 같습니다.")
else :
    print("line1이 더 깁니다.")
    del(line2)
'''
