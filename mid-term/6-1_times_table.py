'''
프로그램 이름 : 구구단(곱셈표)
프로그램 설명 : 7단을 제외한 2단부터 9단의 곱셈표를 출력한다.
'''

for i in range(2, 10, 1) :
    for j in range(2, 10, 1) :
        if j % 7 == 0 : #7단 건너뛰기
            continue
        
        print(j, 'x', i, '=', (j * i), '\t', end = '')
    print()
    
'''
#세로출력
for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print("%d x %d = %d" %(i, j, i*j))
print("")

#가로출력
for i in range(2, 10, 1) :
    print("%d단 : " %(i), end='')
    for j in range(1, 10, 1) :
        print("\t%d x %d = %2d" %(i, j, i*j), end='')
    print("")
print("")

#세로가로출력
for i in range(1, 10, 1) :
    for j in range(2, 10, 1) :
        print("%d x %d = %d" %(j, i, j*i), end = '\t')
    print("")
'''