'''
일자 : 6주차 (2024.04.12)
범위 : Chapter 07. 리스트, 튜플, 딕셔너리
참고 : https://docs.python.org/ko/3.12/tutorial/datastructures.html
'''
'''
numList = [0, 0, 0, 0]
hap = 0

for i in range(0, 4, 1) :
    numList[i] = int(input("숫자%d : " %(i + 1))) #numList[IndexNumber]
    hap += numList[i]

print("합계 : %d" %(hap))
print("합계 : %d" %(sum(numList)))
print(numList)
'''
numList = []
hap = 0

for i in range(0, 10, 1) :
    numList.append(int(input("숫자%2d : " %(i + 1)))) # List의 맨 마지막 요소로 추가된다.
    hap += numList[i] # 반복문을 활용한 누적

print("합계 : %d" %(hap))
print("합계 : %d" %(sum(numList)))
print(numList)



# List는 서로 다른 데이터도 묶을 수 있다.
mixList = []
mixList.append(100)
mixList.append(3.14)
mixList.append(True)
mixList.append("한빛아카데미")
print(mixList)


numList = [10, 20, 30, 40]

# [10, 200, 201, 30, 40]
numList[1:2] = [200, 201] # 슬라이싱을 사용하여 각 '요소'를 추가
print(numList)

# [10, [200, 201], 30, 40]
numList[1] = [200, 201] # 하나의 요소에 '리스트'를 추가!
print(numList)
