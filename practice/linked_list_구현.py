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
            if node is None:
                return None
        return node

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node


if __name__ == '__main__':
    linked_list = LinkedList(10)

    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)

    print(linked_list.get_node(0))
    linked_list.add_node(0, 1111)
    print(linked_list.get_node(0))
    print("=====")
    print(linked_list.get_node(1).data)
    linked_list.add_node(1, 21)
    print(linked_list.get_node(1).data)
    print(linked_list.get_node(2).data)

    print(linked_list.get_node(50))
    print(linked_list.get_node(110))

    linked_list.print_all()
