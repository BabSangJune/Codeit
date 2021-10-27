grades = {}

# key - value 데이터 삽입
grades["태호"] = 60
grades["영훈"] = 70
grades["동욱"] = 80
grades["현승"] = 90

print(grades)

# key를 이용 value 탐색
print(grades["태호"])

# key를 이용 삭제
grades.pop("태호")

print(grades)