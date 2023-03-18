# 가변인자를 이용한 함수 호출

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름, {0}나이, : {1}".format(name, age), end=" ") # end =
#     print(lang1, lang2, lang3, lang4, lang5)



# 만약 유재석이 할 수 있는 언어가 5개 이상으로 늘어났다. 그러면 함수에 lang6을 추가하고 해야하는데 귀찮다.
# 이런 상황에 쓸 수 있는 것이 가변 인자이다.

def profile(name, age, *language): # *로 시작되는 매개변수를 이용하면 된다.
    print("이름, {0}나이, : {1}".format(name, age), end=" ") # end =
    for lang in language:
        print(lang, end = "")
    print()    

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

''' for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    '''
