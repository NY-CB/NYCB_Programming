# if문

weather = input("오늘 날씨는 어때요? ")

'''
if 조건 :
    실행 명령문
    '''

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요") # if 조건이 아닐 때 다른 조건
else:
    print("오늘은 준비물이 필요없어요.") # 위 조건 다 아닐 때

temp = int(input("기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요, 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("하루를 즐기세요")
elif 0<= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요, 나가지 마세요.")