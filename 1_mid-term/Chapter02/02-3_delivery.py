"""
일자 : 2주차 (2024.03.15)
범위 : Chapter 02. 변수
"""

# 택배 배송 정보 입력하기
name = input("받는 사람 : ")
address = input("주소 : ")
weight = int(input("무게(g) : "))

cost = weight * 5 # g당 5원

print("받는 사람 : %s" %name)
print("주소 : %s" %address)
print("배송비 : %d" %cost)
