'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

# 함수 정의 부분
def operation (symbol, num1, num2) :
    if symbol == '+' :
        return num1 + num2
    elif symbol == '-' :
        return num1- num2
    elif symbol == '*' :
        return num1 * num2
    elif symbol == '/' :
        return num1 / num2
    else :
        print("ERROR! 잘못된 연산기호입니다.")

# 메인 코드 부분
symbol = input("계산 입력 (+, -, *, /,) : ")
num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))

result = operation(symbol, num1, num2)

print("## 계산기 : %d %s %d = %d" %(num1, symbol, num2, result))
