# from ipaddress import NetmaskValueError


# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com

# 규칙1 : http//부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 +_ 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 nav51!

# password = "codevisualstudio"

# print(password[:3]) 
# print(len(password))
# print(password.count("e")))

# print(password[:3], len(password), print(password.count("e"))) 

# url = "http://naver.com"

# password = url.replace("http://" , "")
# password = password[:password.index(".")] # password[0:5] 와 같은 함수.
# realpassword = password[:3] + str(len(password)) + str(password.count("e")) + "!"

# print("{0}의 비밀번호는 {1}입니다.".format(url, realpassword))


"https://www.youtubefuckyeah.com"

url = "https://www.youtubefuckyeah.com"

password = url.replace("https://www." , "")

password = password[:password.index(".")]

realpassword = password[:3] + str(len(password)) + str(password.count("e")) + "!"

print(realpassword)