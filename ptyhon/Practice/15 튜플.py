# 튜플

menu = ("돈까스", "치즈까스")

print(menu[0])
print(menu[1])

menu.add("생선까스")

# 튜플은 새로운 값을 넣거나 뺄 수 없음. 고정된 값만 사용 가능함.

name = "김종국"
age = "20"
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", "20", "코딩")
