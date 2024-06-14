'''
프로그램 이름 : 학점 계산기
프로그램 설명 : 이수학점과 성적을 입력받아 취득학점과 총평점, 그리고 평균평점을 출력한다.
'''

subjectList = ["python", "mobile", "excel"] #교과목명을 저장할 리스트
creditList = [] #이수학점을 저장할 리스트
markList = []   #성적(등급)을 저장할 리스트
gradeList = []  #평점을 저장할 리스트
scoreList = []  #평점계를 저장할 리스트

for i in range(len(subjectList)) :
    
    #이수학점 입력 부분
    while True :
        credit = input(subjectList[i] + "의 이수학점 : ")
        
        #이수학점이 숫자가 아닌 경우, 다시 입력 요청
        #<추가개념>isdigit()를 사용하여 0을 포함한 양수로 이루어진 문자나 문자열만 입력받는다.
        if not credit.isdigit() :
            print("[경고] 이수학점을 숫자로 입력하세요.")
            continue
        
        #올바른 입력인 경우 리스트에 추가하고 무한루프 탈출
        creditList.append(int(credit))
        break
    
    #성적 입력 부분
    while True :
        mark = input(subjectList[i] + "의 성적 : ")
        
        #성적이 유효하지 않은 경우, 다시 입력 요청
        #upper()를 사용하여 소문자로 입력 시에도 정상 동작되며, 최종적으로 대문자로 저장한다.
        if mark.upper() not in ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'] :
            print("[경고] 올바른 성적을 입력하세요.")
            continue
        
        #올바른 입력인 경우 리스트에 추가하고 무한루프 탈출
        markList.append(mark)
        break
    
    #성적을 평점으로 변환하여 평점 리스트에 추가
    if mark.upper() == 'A+' :
        gradeList.append(4.5)
    elif mark.upper() == 'A' :
        gradeList.append(4)
    elif mark.upper() == 'B+' :
        gradeList.append(3.5)
    elif mark.upper() == 'B' :
        gradeList.append(3)
    elif mark.upper() == 'C+' :
        gradeList.append(2.5)
    elif mark.upper() == 'C' :
        gradeList.append(2)
    elif mark.upper() == 'D+' :
        gradeList.append(1.5)
    elif mark.upper() == 'D' :
        gradeList.append(1)
    elif mark.upper() == 'F' :
        gradeList.append(0)
    
    #평점계 : 이수학점 * 평점
    scoreList.append(creditList[i] * gradeList[i])

#취득학점
credit = sum(creditList)                   #sum(리스트명) : 리스트의 요소의 핪을 구한다.
print("\n취득학점 ===> ", credit)

#총평점
score = sum(scoreList)                     #sum(리스트명) : 리스트의 요소의 핪을 구한다.
print("총평점 ===> ", score)

#평균평점 : 총평점 / 취득학점
avg = score / credit
print("평균평점 ===> ", round(avg, 2))      #round(변수명, 자릿수) : 실수형 변수의 소수점을 자릿수만큼 반올림한다.
