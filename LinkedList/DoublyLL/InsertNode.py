class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    # Add Node After
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
            cur = cur.next

    # Add Node Before
    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                PREV = cur.prev
                PREV.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = PREV
            cur = cur.next


print("Add Node E After Node A:")
dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("C")
dllist.add_after_node("A", "E")
dllist.print_list()
print("\n")
print("Add Node G before Node A:")
dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("C")
dllist.append("D")
dllist.add_before_node("A", "G")
dllist.print_list()
print("")
