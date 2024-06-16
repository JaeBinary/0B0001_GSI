'''Ch.07 필요 개념 summary'''
# 리스트란? 여러 개의 데이터를 한꺼번에 담을 수 있는 자료구조다. + 대괄호로 묶고 인덱스로 접근
## 리스트명 = []

# 튜플이란? 읽기 전용의 리스트다. + 생략 or 소괄호로 묶고 인덱스로 접근
## 튜플명 = (값1, ···)
## 튜플명 = 값1, ···

'''튜플과 리스트의 상호 변환 p.220'''
myTuple = (10, 20, 30)          # myTuple(튜플) 선언
myList = list(myTuple)          # myList(리스트) 선언과 동시에 myTuple을 리스트로 형변환 후 myList 초기화
myList.append(40)               # myList는 리스트이기에 append 메서드로 쓰기 가능!
myTuple = tuple(myList)         # 기존 myTuple 값에서 '40'을 추가한 myList를 튜플로 형변환 후 저장
print(myTuple)                  # [출력화면] : (10, 20, 30, 40)
