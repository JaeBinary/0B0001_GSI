'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 05. 조건문
'''

ss = input("문자열을 입력하시오. : ")

#모든 문자열이 대문자이면 참
if ss.isupper() :
    print("소문자로 변경 : %s" %(ss.lower()))
else :
    print("대문자로 변경 : %s" %(ss.upper()))
