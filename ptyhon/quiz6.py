# 표준 체중을 구하는 프로그램을 작성하시오.

def std_weight(height, gender):

    man_weight = height * height * 22
    woman_weight = height * height * 21

    if gender == "man":
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, man_weight))
    else:
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height, woman_weight))  
    
# std_weight(1.75, "woman")

def std_weight(height, gender):

    if gender == "man":
       return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "man" 
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
