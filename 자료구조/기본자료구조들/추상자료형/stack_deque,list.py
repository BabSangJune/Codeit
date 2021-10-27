# deque는 파이썬 collections 모듈에서 가지고온다
# 데큐는 더블드링크드리스트
# list를 써도 시간 복잡도가 똑같다
from collections import deque

stack = deque()

# 큐의 맨 끝에 데이터 삽입
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

# 넣은 차례로 출력
print(stack)

# 스택의 맨 뒤 접근
print(stack[-1])

# 맨 뒤 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)