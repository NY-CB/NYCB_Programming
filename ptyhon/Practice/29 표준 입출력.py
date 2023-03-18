# 이전에는 print를 써서 사용을 했었음

print("Python", "Java", "Javascript", sep = ",", end = "?")

print("무엇이 더 재미있을까요?")

# end의 의미는 문장의 끝 부분을 ?로 만들어달라는 뜻.

import sys

print("Python", "Java", file = sys.stdout) # 표준 출력으로 나온다.
print("Python", "Java", file = sys.stderr) # 표준 에러로 나온다. --> 에러가 뜨니까 체크가 필요할 때 해두면 좋다.

# 출력 포맷

scores = {"수학":0, "영어":50, "코딩": 100}

for subject, score in scores.items():
    #key     value
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # ljust(n) 왼쪽부터 문자 포함 n칸의 공간 확보 / rjust(n) 오른쪽부터 n칸의 공간 확보

# 은행에서의 대기 순번표 -> 001, 002, 003, 004,,,,

for number in range(1,21):
    print("대기번호 : " + str(number).zfill(3))
    # zfill(n) n크기 만큼의 값을 집어넣는데 값이 없는 빈 공간에 대해서는 0을 채워넣으라는 말

# 표준 입력

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.") 
# 숫자나 문자 잘 나오는데 여기서의 answer 값은 모두 str로 나오고 있음.
# 사용자의 입력을 통해서는 "항상" 문.자.열의 값(str)으로 나온다는 것을 알 수 있음.





















# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #items()를 하면 사전 데이터에서 key와 value를 가지고 올 수 있다.
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")

# # ljust() 왼쪽에서부터 몇 칸을 확보하고 왼쪽 정렬 / rjust() 오른쪽에서부터 몇 칸을 확보하고 오른쪽 정렬.

# # 은행에 갔을 때 대기 순번표
# # 001, 002, 003 ... 

# # for number in range(1,21):
# #     print("대기번호 : " + str(number))

# # 정렬을 하고싶다면
# for number in range(1,21):
#     print("대기번호 : " + str(number).zfill(3)) #zfill() n개 만큼의 크기, 공간을 확보하고 값을 넣는데 값이 없으면 0을 채워달라는 함수.

# answer = input("아무 값이나 입력하세용 : ") 
# print("입력하신 값은 " + answer + "입니당.") 

# # 숫자를 쓸 때는 str을 써야 하는데 그냥 적어도 출력이 된다.
# # 사용자 입력을 통해서 값을 입력하면 항상 문자열로 받아들이게 된다는 뜻임
