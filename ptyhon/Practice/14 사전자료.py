# 사전

# key와 value 형태 - 목욕탕 키 열쇠를 생각하면 된다.

cabinet = {3:"유재석", 100:"김태호"}   # {Key : Value} 식으로 데이터가 들어감

print(cabinet[3])

print(cabinet[100])

# 사전 자료에서 데이터 불러오기

print(cabinet.get(3))

#print(cabinet.[5]) # 대괄호 [] 를 사용해서 데이터에 없는 값을 입력하면 프로그램이 종료되버린다. 뒤에 값은 안나옴.

print(cabinet.get(5, "사용가능")) #get 함수를 쓰면 None이 나오고 뒤의 함수값도 나온다.

print("hi")

print(3 in cabinet) # 데이터 안에 값이 있는지 확인하는 변수. "in" true / false 로 나옴

cabinet = {"A-3":"유재석", "B-100":"김태호"} 

print(cabinet["A-3"])

# 새 손님

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"

print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

# 총 사용중인 key 출력

print(cabinet.keys())

# 총 사용중인 value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()

print(cabinet)