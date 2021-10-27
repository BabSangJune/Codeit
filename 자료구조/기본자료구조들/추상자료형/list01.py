# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "00")
trending.insert(1, "01")
trending.insert(2, "02")
trending.insert(3, "03")

#출력
print(trending)

print(trending[0])
print(trending[1])

#값 바꾸기
trending[2] = 4

print(trending)

# in 을 이용한 탐색
print("00" in trending)
print("02" in trending)

del trending[0]
print(trending)