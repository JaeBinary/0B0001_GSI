'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

# 함수 정의 부분
def func1() :
    #global a
    a = 10  # 지역변수
    print("func1()에서의 a의 값 :" , a)

def func2() :
    print("func2()에서의 a의 값 :" , a)
    
# 전역변수 선언 부분
a = 20      # 전역변수

# 메인 코드 부분
func1()
func2()
