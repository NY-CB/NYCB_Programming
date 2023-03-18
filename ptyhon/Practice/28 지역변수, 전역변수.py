# 지역변수 - 특정 함수에서만 사용되고 마는 함수
# 전역변수 - 모든 프로그램 내에서 사용되는 함수.

gun = 10

def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용.
    gun = gun - soldiers #여기의 gun은 바깥의 gun이 아닌 이 함수 내에서 설정된 gun임.
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))

checkpoint(2) # 2명이 경계 근무 나감.

print("남은 총 : {0}".format(gun))

# 전역 변수를 계속 쓰게 되면 코드 관리에 어려움이 있기 때문에 권장하지는 않음

def checkpoint_re(gun, soldiers):
    gun = gun - soldiers
    return gun