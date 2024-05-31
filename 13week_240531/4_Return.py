'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

# 함수 정의 부분
def func3() :
    result1, result2 = 100, 200
    return result1, result2

# 전역변수 선언 부분
num1, num2 = 0, 0

# 메인 코드 부분
num1, num2 = func3()
print("func3()에서 돌려준 값 ==>", num1, num2)
