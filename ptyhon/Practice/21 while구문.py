# while 구문
# 5 번 불렀는데 안오면 버리는 정책을 만들었다고 가정

customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았아요.". format(customer, index))
    index -= 1 # -= 한 번씩 줄여나간다는 뜻.
    if index == 0:
        print("커피는 폐기처분되었습니다.")


customer = "아이언맨"
index = 1
while True:
    # print("{0}, 커피가 준비 되었습니다. 호출 {1}회". format(customer, index))
    # index += 1 # 무한 루프인데 정지하려면 컨트롤 C
# 조건이 만족할 때까지 반복하라

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.". format(customer))
    person = input("이름이 어떻게 되세요? ")
    