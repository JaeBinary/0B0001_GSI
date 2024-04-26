while True :
    # 한 번에 여러 값을 입력 받는다. : split() -> 문자열을 공백으로 기준을 나눈다.
    num1, operator, num2 = input("연산식을 입력하세요(ex: 10 + 20):").split()

    # input함수로 입력 받은 숫자는 문자열이므로 정수로 "캐스팅"
    num1 = int(num1)
    num2 = int(num2)

    # num1, num2를 문자열에서 정수로 변환하였으므로 정상적으로 계산 값이 나온다.
    if operator == '+' :
        result = num1 + num2
        print(num1, operator, num2, "=", result)
    elif operator == '-' :
        result = num1 - num2
        print(num1, operator, num2, "=", result)
    elif operator == '*' :
        result = num1 * num2
        print(num1, operator, num2, "=", result)
    elif operator == '/' :
        if num2 == 0 :  #0으로 나눌 경우
            print("0으로 나눌 수 없습니다.")
        else :
            result = num1 / num2
            print(num1, operator, num2, "=", result)
    elif operator == '%' :
        if num2 == 0 :  #0으로 나눌 경우
            print("0으로 나눌 수 없습니다.")
        else :
            result = num1 % num2
            print(num1, operator, num2, "=", result)
    elif operator == '**' :
        result = num1 ** num2
        print(num1, operator, num2, "=", result)
    else :
        print("산술연사자가 아닙니다. 반복문을 종료합니다.")
        break
