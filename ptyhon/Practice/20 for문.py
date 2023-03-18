print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

#randrange()

for waiting_no in range(1,6): # 1,2,3,4,5 라는 리스트 내에 값들을 하나씩 돌아가면서 
    print("대기번호 : {0}.".format(waiting_no))


starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    