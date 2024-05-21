'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 05. 조건문
'''

num = int(input("숫자를 입력하시오. : "))

#많이 쓰이진 않는 중첩 if
if num > 100 :
    if num < 1000 :
        print("100보다 크고 1000보다 작다.")
    else :
        print("1000보다 크다.")
else :
    print("100보다 작다.")
