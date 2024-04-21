'''
일자 : 3주차 (2024.03.22)
범위 : Chapter 03. 연산자
'''
#이수학점
python, mobile, excel = 3, 2, 1

#평균학점
avg = ((python * 3.5) + (mobile * 4) + (excel * 4.5)) / (python + mobile + excel)

print("평점 : ", avg) #소수점 16자리 
print(type(avg))

print("평점 : %f" %(avg)) #소수점 6자리
print(type(avg))

#질문? 배정도 vs 단정도
