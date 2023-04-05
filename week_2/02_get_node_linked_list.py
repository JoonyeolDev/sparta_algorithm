class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        node = self.get_node(index)
        cur = node.next
        node.next = Node(value)
        node.next.next = cur
        return "index 번째 Node 뒤에 value 를 추가하세요!"


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data)