'''비밀번호 생성하기 p.266'''
## 함수 정의 부분
def checkPassword(pwd):
    if len(pwd) < 8:
        return False
    
    if ' ' in pwd:      # 띄어씌기가 있을 때
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
isalpha : 알파벳인지 확인
isdigit : 숫자인지 확인
isalnum : 알파벳 or 숫자인지 확인
'''




'''
## 함수 정의 부분
def checkPassword(pwd) :
    if len(pwd) < 8 :
        return False
    
    if pwd.isalnum() :  # 알파벳 or 숫자일 때
        return True
    else :              # 알파벳 or 숫자가 아닐 때
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
