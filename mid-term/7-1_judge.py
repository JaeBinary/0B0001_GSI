'''
프로그램 이름 : 심사위원 점수 결과 구하기
프로그램 설명 : 심사위원의 평가 점수를 입력받아 평균 점수를 계산합니다.
'''

score = []   #심사위원의 평가 점수를 저장할 리스트를 초기화한다.

#5명의 심사위원이 평가한 점수를 입력받는다.
for i in range(5):
    score.append(int(input("평가 점수 : ")))

avg = sum(score) / 5                   #평균 점수를 계산한다.
print("심사위원 평균 점수 ===>", avg)   #평균 점수를 출력한다.
