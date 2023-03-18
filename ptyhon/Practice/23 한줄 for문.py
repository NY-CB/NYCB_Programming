# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함. -> 101, 102, 103...

students = [1,2,3,4,5]

students = [i+100 for i in students] # i 에다가 100을 더한 값을 넣을텐데 i는 students 안에 있는 값들을 불러오면서 100을 더할 것이야 라는 의미

print(students)

# 학생 이름을 길이로 변환

students = ["Iron man", "Thor", "I am Groot"]

students = [len(i) for i in students]

print (students)

students = ["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
