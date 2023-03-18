from random import *

# 조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample 을 활용

#조건 1
comments = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#조건 2

print(sample(comments, 1))

print("치킨 당첨자 " + str(sample(comments, 1)) +  "축하합니다 ^~^ ")

print("커피 당첨자 " + str(sample(comments, 3)) +  "축하합니다 ^~^ ")

#--------------------------------------------------------------------------------------

users = range(1, 21) # 1부터 20까지 숫자를 생성

#print(type(users)) # range 데이터가 됨. List 데이터로 사용해야하는 퀴즈라서 list로 변경해야함.

users = list(users)
print(users)

#print(type(users))

shuffle(users)
print(users)

# 중복을 줄이기 위해 1명을 뽑고 
winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print(winners)
print(" --- 당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winners[0])) # [0] 첫번째 사람.
print("커피 당첨자 : {0}".format(winners[1:])) # [1:] 나머지 사람들.
print(" --- 축하합니다 ^~^ ---")


# '''
# 1. 숫자를 생성하는데 range로 x 부터 y까지 를 만들 수 있다. # range 함수 사용
# 2. range 함수로 데이터를 생성해도 순서대로인 range 데이터라서 list 데이터로 변경해야한다. # data = list(data) 함수 사용
# 3. list 데이터로 변경되었으나 순서대로이기 때문에 숫자를 마구잡이로 섞는 함수를 사용한다. from random import * 를 적고, 
# suffle(data) 함수를 사용
# 4. 섞은 데이터에서 4개의 값을 뽑아내기 위해 sample 함수를 사용한다. sample(data, 4) - 셔플된 데이터들에서 4개를 가져간다는 뜻
# 5. ("치킨 당첨자 : {0}".format(winners[0])) 의 뜻은 {0} = 컴퓨터 인식으로 winners의 첫번째 위치의 데이터를 불러오는 것.