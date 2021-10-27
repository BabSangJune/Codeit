class Node:
    """노드 클래스 정의"""

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# 노드 생성
root_node = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")

# 각 노드의 자식 생성
root_node.left_child = node_B
root_node.right_child = node_C

node_B.left_child = node_D
node_B.right_child = node_E

node_C.right_child = node_F

node_E.left_child = node_G
node_E.right_child = node_H

# 실행 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)