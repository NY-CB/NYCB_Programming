# 리스트 - 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명


subway = [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]

# #조세호이 몇 번째 칸에 타고 있는가?

# print(subway.index("조세호"))

# 다음 정류장에서 하하가 탔다.

subway.append("하하") #append - 더하는 함수

# # 정형돈을 유재석, 조세호 사이에 태워봄

subway.insert(1, "정형돈")
print(subway)
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# pop 뒤에서 꺼냄

# print(subway.pop())

# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기

subway.append("유재석")

print(subway.count("유재석")) # 같은 값이 몇 번 나오는지 확인하는 함수

#정렬도 가능함

num_list = [5,2,4,3,1]

num_list.sort()
print(num_list)

# 순서 뒤집기도 가능

num_list.reverse()
print(num_list)
# 값들을 모두 지우고 싶다.

num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용 가능함.

mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장

num_list.extend(mix_list)

print(num_list)
