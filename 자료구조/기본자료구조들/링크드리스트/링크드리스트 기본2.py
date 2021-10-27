class Node:
    # 링크드 리스트 노드 클래스
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #링크드 리스트 클래스
    def __init__(self):
        # 처음에는 none
        self.head = None
        self.tail = None

    # 링크드 리스트 추가 연산 메소드
    def append(self, data):
        # Node 만들기
        new_node = Node(data)

        # 링크드 리스트가 비어있을때 (헤드가 비어있음 )
        if self.head is None:
            #헤드랑 테일을 전부 new_node로 설정
            self.head = new_node
            self.tail = new_node
        
        # 비어있지 않을때
        else:
            # 기존 tail의 next에 new 넣고 tail을 new로 바꾸기
            self.tail.next = new_node
            self.tail = new_node

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)


iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next