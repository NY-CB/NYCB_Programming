# 함수의 기본 값 설정하기

def profile(name, age, main_lang):
    print("이름: {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 학년, 반, 수업일 때.
# 기본 값을 세팅하면 된다.

def profile(name, age = 17, main_lang = "파이썬"): #기본값을 설정한다.
    print("이름: {0}, 나이 : {1}, 주 사용 언어: {2}"\
        .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")
