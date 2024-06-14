'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 05. 조건문
'''

score = int(input("점수를 입력하시오. : "))

if score >= 90 :
    print("A", end = '')
elif score >= 80 :
    print("B", end = '')
elif score >= 70 :
    print("C", end = '')
elif score >= 60 :
    print("D", end = '')
else :
    print("F", end = '')
    
print("학점")
