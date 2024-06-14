'''
일자 : 7주차 (2024.04.19)
범위 : Chapter 07. 리스트, 튜플, 딕셔너리
'''

'''
numList2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]

for i in range(0, 3) :
    for j in range(0, 4) :
        print(numList2[i][j], end = '\t')
    print()
'''

#중간고사 변경하여 출제
'''
result = 0

for i in range(0, 5) :
    score = int(input("평가 점수 : "))
    result += score

print("평균 점수 : %d" %(result / (i + 1)))
'''

score = [0, 0, 0, 0, 0]
hap = 0

for i in range(0, 5) :
    score[i] = int(input("평가 점수 : "))
    hap += score[i]
print("평균 점수 : %d" %(hap / 5))
