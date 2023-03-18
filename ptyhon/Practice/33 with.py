# # with 파일 열고 처리하고 닫기까지 했지만 with를 쓰면 조금 더 편하게 할 수 있다.

# import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file)

# # #close 필요없음

# with open ("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있으요.")
# # 파일 쓰는거 두문장

# with open ("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())
# # 파일 읽는거 두문장

# # 깔-끔


import pickle

with open("profile.pickle", "rb") as profile_file: #profile.pickle이라는 피클 데이터를 열고, 이 파일 정보를 profile_file이라는 변수에다가 저장하겠다는 뜻
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding= "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding= "utf8") as study_file:
    print(study_file.read())
    