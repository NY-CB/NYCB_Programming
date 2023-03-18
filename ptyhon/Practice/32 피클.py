# ''' pickle 프로그램 상에서 사용하고 있는 데이터를 파일로 저장하는 것 '''


# import pickle
# profile_file = open("profile.pickle", "wb")
# profile ={"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file 에 저장
# profile_file.close()

# # 피클을 쓰기 위해서는 binary 타입을 정의해줘야함
# # 그래서 "wb" 를 사용한 것.

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기

# print(profile)
# profile_file.close()


import pickle
profile_file = open("profile.pickle", "wb") # "wb"는 쓰는데 binary 타입을 설정할 것이라는 뜻, 따로 인코딩은 필요 없음

profile= {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]} # 사전 형태{}
print(profile)
pickle.dump(profile, profile_file) # 프로필에 있는 정보를 파일에 저장하겠다는 뜻.
profile_file.close()

# 파일에서 데이터를 가지고 오는 예제
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
