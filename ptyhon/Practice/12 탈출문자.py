#탈출문자

# \n : 줄바꿈

print("백문이 불여일견 \n백견이 불여일타") 

# \" 혹은 \' 는 문장 내에서 따옴표를 사용할 수 있게 해줌.
# 저는 "뉴욕치즈버거"입니다.
print("저는 '뉴욕치즈버거'입니다.") 

print('저는 "뉴욕치즈버거"입니다.') #''를 쓰고 안에 ""를 써도 문장 출력은 정상적으로 이루어지긴 하지만 찝찝함.

print("저는 \"뉴욕치즈버거\"입니다.")

# \\ : 문장 내에서 \로 바뀌게 됨.

# print("C:\Users\NYCB\Desktop\PythonWorkspace>") # 이렇게 쓰면 파일 출처라서 이 때는 \\로 변경하면 된다.

print("C:\\Users\\NYCB\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동

print("Red Apple\rPine") #Red Apple -> Pine Apple

#\b : 백스페이스 (한 글자 삭제)

print("Redd\bApple")

#\t : 탭 역할
print("Red\tApple")