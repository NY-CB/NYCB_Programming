# 에러가 발생했을 때 처리하는 것.


try:

    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err) # 어떤 종류의 에러인지 문장으로 표현해준다.

except Exception as err:
    print("알 수 없는 에러가 발생했습니다.")
    print(err)
# try 안에 있는 문장은 실행이 되다가 에러가 떴을 때 except 가 있는 문장을 찾는다.
# try 안에 있는 해당 에러의 종류를 찾은 다음 except의 print를 띄워준다.