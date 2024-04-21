'''
프로그램 이름 : 심사위원 점수 결과 구하기
프로그램 설명 : 
'''

score = []

for i in range(5) :
    score.append(int(input("평가 점수 : ")))

#평균 점수
avg = sum(score) / 5
print("평균 점수 :", avg)