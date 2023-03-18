python = "Python is Disgusting"

print(python.lower()) #lower - 모든 텍스트 소문자

print(python.upper()) #upper - 모든 텍스트 대문자

print(python[0].isupper()) #isupper - n번째 텍스트가 대문자인지 확인 true / false

print(python[0].islower())

print(len(python)) #len() 글자의 갯수

print(python.replace("Python" , "Java"))

index = python.index("n")
print(index)

index = python.index("n", index +1) # n이 나오는 위치에서 시작해서 그 다음에 또 n이 어디에 나오는지 보는 코드
print(index)

print(python.find("n"))
print(python.find("Java")) #find 함수에서 만약 찾는 텍스트가 없다면 -1로 변환해서 알려줌
#print(python.index("Java")) #index 함수에서 만약 찾는 텍스트가 없다면 오류를 내버림. 그 뒤로 무슨 함수를 써도 출력이 안됨.

print(python.count("n"))