'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 04. 데이터형과 문자열
'''
'''
일자 : 5주차 (2024.04.05)
범위 : Chapter 04. 데이터형과 문자열
'''
#중간고사 문제
ss = input("문자열을 입력하시오. : ")

string = ''

for ch in ss : #ss == "입력한 문자열"
    if ch.isupper() :
        string += ch.lower() #대문자를 소문자로 변경
    else : #ch.islower
        string += ch.upper() #소문자를 대문자로 변경
        
print("변경된 문자열 : %s" %(string))

''' ss[i]는 객체가 아니기에 .lower() 접근이 불가능하다.
for i in range(len(ss)) :
    print(i)
    if ss[i].isupper() :
        ss[i] = ss[i].lower() #대문자를 소문자로 변경
    else : #ss[i].islower
        ss[i] = ss[i].upper() #소문자를 대문자로 변경
        
print("변경된 문자열 : %s" %(ss))
'''
