'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

# 함수 정의 부분
def addition (num1, num2) :                     # 덧셈 기능을 수행하는 함수 정의
    return num1 + num2

def subtraction (num1, num2) :                  # 뺄셈 기능을 수행하는 함수 정의
    return num1 - num2

def multiplication (num1, num2) :               # 곱셈 기능을 수행하는 함수 정의
    return num1 * num2

def division (num1, num2) :                     # 나눗셈 기능을 수행하는 함수 정의
    return num1 / num2

# 전연벽수 선언 부분
num1, num2, operation = 0, 0, ''

# 메인 코드 부분
while True :
    operation = input("계산 입력 (+, -, *, /,) : ")
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))

    if operation == '+' :
        result = addition(num1, num2)           # 덧셈 기능을 수행하는 함수 호출
    elif operation == '-' :
        result = subtraction(num1, num2)        # 뺄셈 기능을 수행하는 함수 호출
    elif operation == '*' :
        result = multiplication(num1, num2)     # 곱셈 기능을 수행하는 함수 호출
    elif operation == '/' :
        result = division(num1, num2)           # 나눗셈 기능을 수행하는 함수 호출
    else :
        print("ERROR! 연산자를 잘못 입력하여 프로그램을 종료합니다.")
        break

    print("## 계산기 : %d %s %d = %d" %(num1, operation, num2, result))
    print()
