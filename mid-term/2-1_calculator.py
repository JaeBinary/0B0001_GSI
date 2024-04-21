'''
프로그램 이름 : python 산술 연산자를 활용한 계산기
프로그램 설명 : 사용자로부터 두 수와 연산기호를 입력받아 python 산술 연산을 해준다. 종료 시 특정 문자인 'p'를 입력 받아 프로그램을 종료한다.
'''

numList = [0, 0]    #연산할 두 수를 저장한다.
operator = ''       #연산 기호를 저장할 변수를 초기화한다.

numList[0] = float(input("숫자를 입력하시오. : "))              #numList[0]에는 '결과 값'을 저장한다.

#사용자로부터 'p' 문자를 입력받기 전까지 무한 반복된다.
while(operator != 'p') :
    print("\n현재 결과 ===> ", numList[0])  #사용자에게 현재 어떤 값과 연산을 하고 있는 지 보여준다. (중복 연산 시 편의성을 위함.)
    operator = input("연산기호를 입력하시오.(종료 : p) : ")     #operator에는 연산기호를 저장한다.
    
    #사용자로부터 python에서 가능한 연산기호를 입력받을 수 있도록 한다.
    if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '//' and operator != '%' and operator != '**' :
        continue
    
    numList[1] = int(input("숫자를 입력하시오. : "))            #numList[1]에는 '연산될 값'을 저장한다.
    
    if operator == '+' :    #덧셈 연산을 실행한다.
        numList[0] += numList[1]
    elif operator == '-' :  #뺄셈 연산을 실행한다.
        numList[0] -= numList[1]
    elif operator == '*' :  #곱셈 연산을 실행한다.
        numList[0] *= numList[1]
    elif operator == '/' :  #나눗셈 연산을 실행한다.
        numList[0] /= numList[1]
    elif operator == '//' : #몫 연산을 실행한다. : 나눗셈 연산 후 소수점을 버린다.
        numList[0] //= numList[1]
    elif operator == '%' :  #나머지 연산을 실행한다.
        numList[0] %= numList[1]
    elif operator == '**' : # 거듭제곱 연산을 실행한다.
        numList[0] **= numList[1]

print("\n최종 결과 ===> ", numList[0])  #프로그램 종료 전 최종 결과 값을 출력한다.