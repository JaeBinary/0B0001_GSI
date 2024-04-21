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
    
    #이수학점과 성적을 append()를 통해 각 리스트 요소로 추가한다.
    creditList.append(int(input(subjectList[i] + "의 이수학점 : ")))
    markList.append(input(subjectList[i] + "의 성적 : "))
    
    #성적을 upper()를 통해 대소문자를 구분하지 않고 평점으로 변환한다.
    if markList[i].upper() == 'A+' :
        gradeList.append(4.5)
    elif markList[i].upper() == 'A' :
        gradeList.append(4)
    elif markList[i].upper() == 'B+' :
        gradeList.append(3.5)
    elif markList[i].upper() == 'B' :
        gradeList.append(3)
    elif markList[i].upper() == 'C+' :
        gradeList.append(2.5)
    elif markList[i].upper() == 'C' :
        gradeList.append(2)
    elif markList[i].upper() == 'D+' :
        gradeList.append(1.5)
    elif markList[i].upper() == 'D' :
        gradeList.append(1)
    else :
        gradeList.append(0)
    
    #평점계 : 이수학점 * 평점
    scoreList.append(creditList[i] * gradeList[i])

#취득학점
credit = sum(creditList)    #sum(리스트명) : 리스트의 요소의 핪을 구한다.
print("\n취득학점 ===> ", credit)

#총평점
score = sum(scoreList)      #sum(리스트명) : 리스트의 요소의 핪을 구한다.
print("총평점 ===> ", score)

#평균평점 : 총평점 / 취득학점
avg = score / credit
print("평균평점 ===> ", round(avg, 2))      #round(변수명, 자릿수) : 실수형 변수의 소수점을 자릿수만큼 반올림한다.