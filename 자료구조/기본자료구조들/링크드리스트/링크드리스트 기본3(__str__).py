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

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)