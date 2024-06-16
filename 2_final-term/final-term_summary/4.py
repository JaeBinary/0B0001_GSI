'''100일 기념일 날짜 구하기 p.265'''
from datetime import datetime, timedelta

## 함수 정의 부분
def getAfterDate(start_date, days):
    retDate = start_date + timedelta(days=days)
    return retDate

## 전역변수 선언 부분
input_date = ''
start_date, after_date = None, None

## 메인 코드 부분
while(True) :
    input_date = input("날짜를 입력하세요 (YYYY-MM-DD) : ")

    try:
        start_date = datetime.strptime(input_date, "%Y-%m-%d")  # 입력 형식 변경할 경우 (input_data, "%Y.%m.%d")
        print("입력한 날짜\t==>\t", start_date)
        after_date = getAfterDate(start_date, 100)  # 시작일부터 1일로 할 경우 (start_date, 99)
        print("100일 후 날짜\t==>\t", after_date)
        break
    except ValueError:
        print("잘못된 날짜 형식입니다. YYYY-MM-DD 형식으로 입력해주세요.")

'''URL : https://docs.python.org/ko/3/library/datetime.html#strftime-strptime-behavior
%y : 두 자리 수의 연도 ex) 19, 20, 21
%Y : 네 자리 수의 연도 ex) 2019, 2020, 2021

%m : 0을 채운 두 자리 수의 월 ex) 01, 02 ...  11 ,12

%d : 0을 채운 두 자리 수의 일 ex) 01, 02 ...  30, 31

%I : 0을 채운 12시간제의 시간 ex) 01, 02 … 12

%H : 0을 채운 24시간제의 시간 ex) 00, 01 … 23

%M : 0을 채운 두 자리 수의 분 ex) 00, 01 ... 58, 59

%S : 0을 채운 두 자리 수의 초 ex) 00, 01 ... 58, 59
'''



'''
from datetime import datetime, timedelta

## 함수 정의 부분
def getCurrent() :
        curDate = datetime.now()
        return curDate

def getAfterDate(now, day) :
    retDate = now + timedelta(days=day)
    return retDate

## 전역변수 선언 부분
nowDate, afterDate = None, None

## 메인 코드 부분
nowDate = getCurrent()
print("현재 날짜와 시간\t==>\t", nowDate)
afterDate = getAfterDate(nowDate, 100)
print("100일 후 날짜와 시간\t==>\t", afterDate)
'''