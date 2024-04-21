'''
프로그램 이름 : 영문 알파벳 대소문자 변환기
프로그램 설명 : 알파벳의 짝수번째 글자를 대문자를 변경하고 홀수번째는 소문자로 변경한다.
'''

charList =[]
string = "ABcdEFGhijklNMOpqrstuvwxyz" #input("문자열을 입력하시오. : ")
change = ''

for i in string :
    charList.append(i)

for i in range(len(charList)) :
    if((i + 1) % 2 == 0) : #짝수번째 글자 대문자로 변경
        change += charList[i].upper()
    else :
        change += charList[i].lower()

print(change)

'''
lower()는 문자열의 모든 문자를 소문자로 바꾼다.
upper()는 문자열의 모든 문자를 대문자로 바꾼다.
swapcase()는 대문자를 소문자로, 소문자를 대문자로 바꾼다.
capitalize()는 문자열의 첫 번째 문자만 대문자로 바꾸고 나머지 문자를 소문자로 바꾼다. 
title()는 문자열의 각 단어 첫 번째 문자를 대문자로 바꾼다.
'''