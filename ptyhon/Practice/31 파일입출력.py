score_file = open("score.txt", "w", encoding = "utf8") 

# "w" 는 파일에 무엇을 쓰기위한 목적으로 열겠다라고 정의해줌.
# UTF8은 한글을 쓸 수 있게 해주는 파일이므로 항상 쓰는 것을 추천.

print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)

score_file.close()
# open 했으면 close도 해야함.

score_file = open("score.txt", "a", encoding = "utf8") # append 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "") # 한 줄만 읽는 것. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "") 
print(score_file.readline(), end = "") 
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline() #무한 루프를 만드는데 한 줄씩 읽을거다
    if not line: #근데 내용이 없으면
        break #반복문 탈출한다
    print(line)
score_file.close()

# list에 값을 넣어서
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

















# score_file = open("score.txt", "a", encoding = "utf8")

# # "a" 는 append 즉 덮어쓰기를 쓰겠다는 의미

# score_file.write("과학: 80")
# score_file.write("\n코딩: 100") # 줄바꿈이 자동으로 안되서 \n을 집어 넣어서 강제로 줄바꿈을 해줌.
# score_file.close()

# score_file = open("score.txt", "r", encoding= "utf8")

# print(score_file.read())
# score_file.close()
# # 모두 다 불러오는 것
# #"r"은 read의 r, 파일을 읽어 오겠다라는 의미.

# score_file = open("score.txt", "r", encoding= "utf8")

# print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동, 줄바꿈 안하고 싶다면 end = ""
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "")

# score_file.close()

# # 다른 파일이 몇 줄인지 모를 때

# score_file = open("score.txt", "r", encoding= "utf8")
# while True: # 무한루프인데
#     line = score_file.readline()
#     if not line:
#         break # 탈출하기
#     print(line, end = "")

# score_file.close()

# # 리스트에다 값을 넣고 할 수 있음

# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines() #list 형태로 저장하기
# for line in lines: 
#     print(line, end = "")

# score_file.close()
