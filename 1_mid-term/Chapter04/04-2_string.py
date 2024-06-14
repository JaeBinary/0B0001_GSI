'''
일자 : 3주차 (2024.03.22)
범위 : Chapter 04. 데이터형과 문자열
'''

var1 = input("1번째 문자열을 입력하시오. : ")
var2 = input("2번째 문자열을 입력하시오. : ")

#len함수는 문자열의 길이를 파악할 때 사용, 정수형으로 저장된다.
len1 = len(var1)
len2 = len(var2)

diff = len1 - len2

print("두 문자열의 길이 차이는 %d입니다." %(diff))

#upper, lower함수는 문자열 뒤에 사용하거나 변수 뒤에 사용할 수 있다.
var1 = "First Python을 밤 12시까지 열공 중!".upper()
var2 = "First Python을 밤 12시까지 열공 중!".lower()
print("%s\n%s" %(var1, var2))
