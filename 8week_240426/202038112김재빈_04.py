score = []   #심사위원의 평가 점수를 저장할 리스트를 초기화한다.

print("홍길동 선수 경기 끝났습니다~~~ 짝짝짝")

#7명의 심사위원이 평가한 점수를 입력받는다.
for i in range(7):
    score.append(float(input("심사 점수 ==>")))

hap = sum(score)                            #합계 점수를 계산한다.
print("심사위원 합계 점수 :", round(hap, 1))   #합계 점수를 출력한다.

avg = hap / 7                               #평균 점수를 계산한다.
print("심사위원 평균 점수 :", round(avg, 1))   #평균 점수를 출력한다.
