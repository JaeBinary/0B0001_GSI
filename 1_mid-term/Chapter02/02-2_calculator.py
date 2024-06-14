"""
일자 : 2주차 (2024.03.15)
범위 : Chapter 02. 변수
"""

# input함수는 문자열로 저장된다.
# num1 = input("1번째 숫자를 입력하시오. : ")
# num2 = input("2번째 숫자를 입력하시오. : ")

# 한 번에 여러 값을 입력 받는다. : split() -> 문자열을 공백으로 기준을 나눈다.
num1, num2 = input("2개의 숫자를 입력하시오.[num1 num2] : ").split()

# [추가개념] 한 번에 여러 값을 입력 받는다. : split() -> 문자열을 특정문자로 기준을 나눈다.
num1, num2 = map(int, input("2개의 숫자를 입력하시오.[num1, num2] : ").split(','))

# input함수로 입력 받은 숫자는 문자열이므로 정수로 "캐스팅"
num1 = int(num1)
num2 = int(num2)

# num1, num2를 문자열에서 정수로 변환하였으므로 정상적으로 계산 값이 나온다.
result = num1 + num2
print(num1, "+", num2, "=", result)

result = num1 - num2
print(num1, "-", num2, "=", result)

# %문자 : 서식지정자 -> 출력 시 변수나 값으로 대체되는 기능
result = num1 * num2
print("%d x %d = %d" %(num1, num2, result))

result = num1 - num2
print("%d - %d = %d" %(num1, num2, result))
