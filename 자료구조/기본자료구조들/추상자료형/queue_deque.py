# deque는 파이썬 collections 모듈에서 가지고온다
# 데큐는 더블드링크드리스트
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

# 넣은 차례로 출력
print(queue)

# 큐의 가장 앞에 접근
print(queue[0])

# 맨 앞 데이터 삭제
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)