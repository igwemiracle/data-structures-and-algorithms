class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end="")
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("U")
llist.append("T")
llist.insert_after_node(llist.head.next, "O")
llist.print_list()
print("")
