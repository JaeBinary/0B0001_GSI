while True :
    word = input("영단어를 입력하세요 =>")    #사용자로부터 문자열을 입력받는다.

    if word.isalpha() == False :          #입력한 문자열이 영문자가 아닌 경우
        print("영문자가 아닙니다. 반복문을 종료합니다.")
        break
    
    print("대소문자 변경 결과 :", word.swapcase())  #swapcase() : 대문자를 소문자로, 소문자를 대문자로 바꾼다.

print("프로그램을 종료합니다.")
