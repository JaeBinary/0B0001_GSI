'''
일자 : 13주차 (2024.05.31)
범위 : Chapter 08. 함수
'''

import random

# 함수 정의 부분
def lottoFunc() :
    return random.randint(1, 45)

# 전역변수 선언 부분
lottoList = []
num =0

# 메인 코드 부분
print("***** 로또 추첨을 시작합니다. *****")

while True :
    num = lottoFunc()

    if num in lottoList :       # [중복된 숫자일 경우]
        continue                # 번호를 다시 받기 위함.
    else :                      # [새로운 숫자일 경우]
        lottoList.append(num)   # 리스트에 추가위함.

    if len(lottoList) == 6 :    # [6개의 숫자를 받은 경우]
        break                   # 무한 루프를 빠져나오기 위함.

lottoList.sort()    # 숫자를 오름차순으로 정렬하기 위함.
print("오늘의 로또 번호 ==>", lottoList)



'''
print("오늘의 로또 번호 ==>", end = '')
for i in range(0,6) :
    print(lottoList[i], '', end = '')
'''
