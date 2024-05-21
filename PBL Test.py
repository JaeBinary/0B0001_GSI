#편의점의 물품 재고 관리 프로그램
productDict = {"커피음료":7, "펜":3, "종이컵":2, "우유":1, "콜라":4, "책":5}
name = ''
count = 0

while True :
    menu = input("메뉴를 선택하시오 1)재고조회 2)입고 3)출고 4)종료 : ")

    if(menu == '1') :
        name = input("[재고조회] 물건의 이름을 입력하시오 : ")
        if name in productDict:
            print("재고 :", productDict[name])
        else :
            print("해당 제품은 취급하지 않습니다.")

    elif(menu == '2') :
        name, count = input("[입고] 물건의 이름과 수량을 입력하시오 : ").split()
        if name in productDict:
            productDict[name] += int(count)
            print("재고 :", productDict[name])
        else :
            print("해당 제품은 취급하지 않습니다.")

    elif(menu == '3') :
        name, count = input("[출고] 물건의 이름과 수량을 입력하시오 : ").split()
        if name in productDict:
            productDict[name] -= int(count)
            print("재고 :", productDict[name])
        else :
            print("해당 제품은 취급하지 않습니다.")

    elif(menu == '4') :
        print("프로그램을 종료합니다.")
        break

    else :
        print("잘못 선택하셨습니다.")
        continue