while True :
    weight = float(input("체중[Kg] ==> ")) #사용자로부터 체중을 입력받아 저장한다.
    if weight == 0 :    #체중에 0이 입력되면 "EXIT" 출력후 무한루프를 빠져나온다.
        print("EXIT")
        break
    
    height = float(input("신장[cm] ==> ")) #사용자로부터 신장을 입력받아 저장한다.
    height = height / 100 #cm를 m로 변경한다.

    BMI = weight / (height ** 2)           #신체질량지수(BMI) = 체중(kg) / [신장(m)]2
    BMI = round(BMI , 2)                   #round(변수명, 자릿수) : 실수형 변수의 소수점을 자릿수만큼 반올림한다.

    print("당신의 BMI는", BMI, "입니다.")

    if BMI < 18.5:              #저체중 : 18.5kg/㎡ 미만
        print("당신은 저체중입니다.")
    elif 18.5 <= BMI < 23:      #정상 : 18.5 ~ 22.9kg/㎡
        print("당신은 정상체중입니다.")
    elif 23 <= BMI < 25:        #과체중 : 23 ~ 24.9kg/㎡
        print("당신은 과체중입니다.")
    else:                       #비만 : 25kg/㎡ 이상
        print("당신은 비만입니다.")
