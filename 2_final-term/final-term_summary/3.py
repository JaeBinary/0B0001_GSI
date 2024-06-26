'''Ch.08 필요 개념 summary'''
# 지역변수란? 말 그대로 한정된 지역(local)에서만 사용되는 변수
# 전역변수란? 프로그램 전체(global)에서 사용되는 변수

'''기말고사 서술식'''
# 1. 지역변수 사용 시 메모리를 효율적으로 사용할 수 있다.
# 2. 전역변수 사용 시 논리적 오류를 야기할 수 있다.

'''코드 8-10 p.265'''
# 함수 정의 부분
def func1() :
    #global a
    a = 10  # 지역변수
    print("func1()에서의 a의 값 :" , a)

def func2() :
    print("func2()에서의 a의 값 :" , a)
    
# 전역변수 선언 부분
a = 20      # 전역변수

# 메인 코드 부분
func1()
func2()