'''
일자 : 11주차 (2024.05.17)
범위 : Chapter 07. 리스트, 튜플, 딕셔너리
'''

empDict = {"사번":1000, "이름":"홍길동", "부서":"케이팝"}

#in 함수는 딕셔너리의 키의 존재 유무에 따라 True / False를 반환!
print("이름" in empDict)
print("주소" in empDict)



print()
#in 함수는 보통 if문과 같이 사용!
if "이름" in empDict :
    print("이름", empDict["이름"])



print()
#값의 유무를 판별하는 예
if 1000 in empDict.values() :
    print("1000이라는 값이 있습니다.")



print()
#딕셔너리의 키를 카운터변수 key에 하나씩 대입하면서 반복!    
for key in empDict.keys():
    print(key, empDict[key])



print()
'''가수 정보를 딕셔너리에 저장하고 출력하기'''
groupDict = {"이름":"트와이스", "구성원수":9, "데뷔":"서바이벌 식스틴", "대표곡":"CRY FOR ME"}

for key in groupDict.keys():
    print(key, "==>", groupDict[key])
