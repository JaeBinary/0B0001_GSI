'''
일자 : 7주차 (2024.04.19
범위 : Chapter 07. 리스트, 튜플, 딕셔너리
참고 : https://docs.python.org/ko/3.12/tutorial/datastructures.html
'''
'''
numList = []
hap = 0

for i in range(0, 5, 1) :
    numList.append(int(input("숫자%2d : " %(i + 1)))) # List의 맨 마지막 요소로 추가된다.
    hap += numList[i] # 반복문을 활용한 누적

print("합계 : %d" %(hap))
print("합계 : %d" %(sum(numList)))

print(numList)

for i in range(0, 5, 1) :
    print("List의 %d번째 요소 : %d" %(i, numList[i]))
'''

'''
numList = [10, 20, 30, 40]


numList[1:2] = [200, 201]   #슬라이싱을 사용하여 각 '요소'를 추가
print(numList)              #출력 : [10, 200, 201, 30, 40]


numList[1] = [200, 201]     #하나의 요소에 '리스트'를 추가!
print(numList)              #출력 : [10, [200, 201], 201, 30, 40]

numList[1][0] = [100, 101]  #하나의 리스트 요소에 '리스트'를 추가!
print(numList)              #출력 : [10, [[100, 101], 201], 201, 30, 40]

print(numList[0])           #출력 : 10
print(numList[1][0][0])     #출력 : 100
print(numList[1][0][1])     #출력 : 101
print(numList[1][1])        #출력 : 201
print(numList[2])           #출력 : 201
print(numList[3])           #출력 : 30
print(numList[4])           #출력 : 40
'''


numList = [10, 20, 30]
print("numList : ", numList)

print("\n<리스트 값 삽입>")
numList.append(40)      #append(메소드) : 리스트 맨 뒤에 요소에 값을 추가!
print("numList.append(40) : ", numList)             #출력 : [10, 20, 30, 40]
numList.insert(2, 25)   #insert(메소드) : 리스트 원하는 번째의 요소에 값을 추가!
print("numList.insert(2, 25) : ", numList)          #출력 : [10, 20, 25, 30, 40]

#리스트 값 삭제
print("\n<리스트 값 삭제>")
del(numList[2])         #del(표준함수)  : 리스트 및 리스트 요소 삭제!
print("del(numList[2]) : ", numList)                #출력 : [10, 20, 30, 40]
numList.remove(10)      #remove(메소드) : 리스트 요소의 특정 값 삭제! (중복된 값을 지울 때, 처음 만나는 한 개의 값만 삭제!)
print("numList.remove(10) : ", numList)             #출력 : [20, 30, 40]

#리스트 값 변경
print("\n<리스트 값 변경>")
numList[2:] = [10, 10]
print("numList[2:] = [10, 10] : ", numList)         #출력 : [20, 30, 10, 10]

#리스트 값 추출
print("\n<리스트 값 추출>")
num = numList.pop()     #pop(메소드)   : 맨 뒤의 값을 추출! (반환을 해준다.)
print("numList.pop() : ", num)                      #출력 : 10
print(numList)                                      #출력 : [20, 30, 10]

#python 리스트에선 push가 지원 안된다. but, append()와 유사하다.

#리스트 값 세기
print("\n<리스트 값 세기>")
num = numList.count(10) #count(메소드) : 리스트에서 찾을 값이 몇 개인지 개수를 세기!
print("numList.count(10) : ", num)                  #출력 : 1

#리스트 크기
print("\n<리스트 크기>")
print("len(numList) : ", len(numList))

#리스트 값 정렬
print("\n<리스트 값 정렬>")
numList.sort()          #sort(메소드) : 리스트의 요소를 정렬! (default : 오름차순)
print("numList.sort() : ", numList)                 #출력 : [10, 20, 30]
numList.sort(reverse = True)    #내림차순 정렬!
print("numList.sort(reverse = True) : ", numList)   #출력 : [30, 20, 10]

#리스트 값 반전
print("\n<리스트 값 반전>")
numList.reverse()       #reverse(메소드)   : 리스트의 마지막 인덱스부터 위치가 반전!
print("numList.reverse() : ", numList)              #출력 : [10, 20, 30]
