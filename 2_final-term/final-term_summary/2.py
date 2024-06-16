'''Ch.07 필요 개념 summary'''
# 딕셔너리란? 키(Key)와 값(Value)의 쌍이 하나로 묶이는 자료구조다. + 중괄호로 묶고 키(Key)로 접근
# ※ 순서가 없다.
## 딕셔너리명 = {키:값, ···}
## 딕셔너리명[키] = 값

myDict = {'이름':'김재빈'}
myDict['이름'] = '최상현'   # 기존 키에 대한 값 변경 : '이름' : '최상현'
print(myDict)

myDict['최상현'] = '별명'   # 새로운 데이터 추가 : '최상현':'별명'
print(myDict)

'''편의점 재고 관리하기 p.228'''
# 물품 사전 초기화: 각 제품의 이름과 초기 재고 수량을 저장
merchandiseDict = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

# 무한 루프 시작: 사용자가 프로그램을 종료할 때까지 계속 실행
while True:
    # 사용자에게 메뉴 선택을 요청
    menu = input("메뉴를 선택하시오 1)재고조회 2)입고 3)출고 4)종료 : ")

    # 메뉴 1: 재고 조회
    if menu == '1':
        # 조회할 물품의 이름을 입력받음
        name = input("[재고조회] 물품의 이름을 입력하시오 : ")
        
        # 입력한 이름이 물품 사전에 있는지 확인
        if name in merchandiseDict:
            # 물품이 있으면 재고 수량 출력
            print("재고 :", merchandiseDict[name])
        else:
            # 물품이 없으면 에러 메시지 출력
            print("해당 물품은 취급하지 않습니다.")

    # 메뉴 2: 입고
    elif menu == '2':
        # 입고할 물품의 이름과 수량을 입력받음
        name, count = input("[입고] 물품의 이름과 수량을 입력하시오 (예: 콜라 10) : ").split()
        
        # 수량을 정수로 변환
        count = int(count)
        
        # 입력한 이름이 물품 사전에 있는지 확인
        if name in merchandiseDict:
            # 물품이 있으면 재고 수량에 입력받은 수량을 더해줌
            merchandiseDict[name] += count
            # 업데이트된 재고 수량 출력
            print("재고 :", merchandiseDict[name])
        else:
            # 물품이 없으면 새로 추가
            merchandiseDict[name] = count
            # 새로 추가된 물품 및 재고 수량 출력
            print("**", name, "** 새로 추가되었습니다.\n재고 : ", merchandiseDict[name])
            
    # 메뉴 3: 출고
    elif menu == '3':
        # 출고할 물품의 이름과 수량을 입력받음
        name, count = input("[출고] 물품의 이름과 수량을 입력하시오 (예: 콜라 10): ").split()
        
        # 수량을 정수로 변환
        count = int(count)
        
        # 입력한 이름이 물품 사전에 있는지 확인
        if name in merchandiseDict:
            # 현재 재고가 출고할 수량 이상인지 확인
            if merchandiseDict[name] >= count:
                # 재고가 충분하면 재고 수량에서 입력받은 수량을 빼줌
                merchandiseDict[name] -= count
                # 업데이트된 재고 수량 출력
                print("재고 :", merchandiseDict[name])
            else:
                # 재고가 부족하면 에러 메시지 출력
                print("재고가 부족합니다. 현재 재고 :", merchandiseDict[name])
        else:
            # 물품이 없으면 에러 메시지 출력
            print("해당 물품은 취급하지 않습니다.")

    # 메뉴 4: 프로그램 종료
    elif menu == '4':
        # 종료 메시지 출력하고 루프 종료
        print("프로그램을 종료합니다.")
        break

    # 잘못된 메뉴 선택 처리
    else:
        # 잘못된 메뉴 선택 시 에러 메시지 출력하고 루프 계속
        print("잘못 선택하셨습니다.")
