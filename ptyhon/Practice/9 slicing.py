#Slicing

jumin = "971111-1234567"

print("성별 : " + jumin[7])

print("연 : " + jumin[0:2]) #[X:Y] X부터 Y직전까지

print("월 : " + jumin[2:4])

print("일 : " + jumin[4:6])

print("생년월일 : " +jumin[:6]) #처음부터 6 직전까지의 값을 불러온다.

print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지

print("뒤 7자리 (뒤에서부터)" + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지는 -를 붙인다.
