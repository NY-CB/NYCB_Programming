# 교실에서 학생들에게 책을 읽으라고 시키는데 결석을 했을 때

absent = [2,5] #결석
no_book = [7] #책 깜빡함
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent: 
        continue #해당 데이터가 없으면 건너뛰고 계속 진행하는 함수
    elif student in no_book:
        print("너는 뒤졌다 딱대. {0}는 좀 맞자. 퍽퍽퍽.,..".format(student))
        break #해당 데이터가 없으면 반복문을 탈출하는 함수
    print("{0}, 책을 읽어봐라.".format(student))

