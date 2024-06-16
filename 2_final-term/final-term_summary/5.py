'''비밀번호 생성하기 p.266'''
## 함수 정의 부분
def checkPassword(pwd):
    if len(pwd) < 8:
        return False
    
    if ' ' in pwd:
        return False
    
    return True

## 전역변수 선언 부분
password = ''

## 메인 코드 부분
while(True):
    password = input("새로운 비밀번호를 입력하세요 : ")

    if checkPassword(password):
        print("Good~ 비밀번호가 올바르게 생성되었어요")
        break
    else:
        print("오류! 비밀번호가 규칙에 맞지 않습니다")





'''
## 함수 정의 부분
def checkPassword(pwd) :
    if len(pwd) < 8 :
        return False
    
    if pwd.isalnum() :
        return True
    else :
        return False

## 전역변수 선언 부분
password = ''

## 메인 코드 부분
while(True) :
    password = input("새로운 비밀번호를 입력하세요 : ")

    if checkPassword(password) :
        print("Good~ 비밀번호가 올바르게 생성되었어요")
        break
    else :
        print("오류! 비밀번호가 규칙에 맞지 않습니다")
'''
