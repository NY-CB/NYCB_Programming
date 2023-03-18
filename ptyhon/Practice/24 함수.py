# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission
    
balance = 0 #잔액
balance = deposit(balance, 1000)
# balacne = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)

print("수수료 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))
