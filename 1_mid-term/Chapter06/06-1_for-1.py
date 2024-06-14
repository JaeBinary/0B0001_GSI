'''
일자 : 4주차 (2024.03.29)
범위 : Chapter 06. 반복문
'''
#range(시작값, 끝값+1, 증가값) : 증가값 생략 시 default
for i in range(0, 5, 2) :
    print("%d : python" %(i))

for i in range(1, 11, 1) :
    print("%d " %(i), end = '')

print("\n")

#리스트
for i in [8, 1, 5] :
    print("%d : python" %(i))
