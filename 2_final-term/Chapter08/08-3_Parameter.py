'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

# 함수 정의 부분
def para_func(v1, v2, v3 = 0) :
    return v1 + v2 + v3

# 전역변수 선언 부분
result = 0

# 메인 코드 부분
result = para_func(10, 20)      # para_func() 함수의 매개변수인 'v3'가 초기화 되어 있지 않다면, ERROR 발생!
print("매개변수 2개 함수 호출 결과 ==>", result)

result = para_func(10, 20, 30)
print("매개변수 3개 함수 호출 결과 ==>", result)
