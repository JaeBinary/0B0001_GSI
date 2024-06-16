while True:
    while True:
        user_input = input("내부 루프입니다. 'exit'를 입력하면 내부 루프를 종료합니다: ")
            
        if user_input == 'exit':
            print("**************** 내부 루프를 종료합니다. ****************\n")
            break  # 내부 루프 종료
        
    user_input = input("외부 루프입니다. 'exit'를 입력하면 외부 루프를 종료합니다: ")
        
    if user_input == 'exit':
        print("**************** 외부 루프를 종료합니다. ****************\n")
        break  # 외부 루프 종료

print("프로그램이 종료되었습니다.")
