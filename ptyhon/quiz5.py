# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해진다.
# 조건 2: 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야한다.

#출력문 예제
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분


# 조건 1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해진다.

# users = range(1, 51)
# users = list(users)
# print(users)

# time = range(5,51)
# time = list(time)
# shuffle(time)
# print(time)

# from itertools import count
# from random import randrange, shuffle


# for users in range(1,51):

#     time = randrange(5,51)

#     if time < 16:
#         print("[O] {0}번째 손님 (소요시간 : {1} 분)".format(users, time))
#     else:
#          print("[X] {0}번째 손님 (소요시간 : {1} 분)".format(users, time))


# # 조건 2: 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야한다.


from random import *

cnt = 0 # 총 탑승 승객 수

for i in range (1, 51) : # 1 ~ 50 이라는 승객 수
    time = randrange(5,51)
    if 5 <= time <= 15: # 5~15분 이내의 손님, 탑승 승객 수 증가처리
        print("[O] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[X] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))

