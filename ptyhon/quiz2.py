from random import *



print(randrange(4,28)) #1 ~ 46 미만의 임의의 값 생성



# print("오프라인 스터디 모임 날짜는 매월" + print +"일로 선정되었습니다.") 
# randrange는 미만, randint는 이하의 함수
# str을 사용해서 정수로 변환

date = randint(4,28)

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")
