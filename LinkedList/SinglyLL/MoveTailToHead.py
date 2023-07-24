
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
            print(cur_node.data, end=" ")
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

    def move_tail_to_head(self):
      if self.head and self.head.next:
        last = self.head
        second_to_last = None

      while last.next:
        second_to_last = last
        last = last.next

      last.next = self.head
      second_to_last.next = None
      self.head = last

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# A -> B -> C -> D -> Null
# D -> A -> B -> C -> Null
llist.print_list()
print("\nThe tail gets moved to the head of the list")
llist.move_tail_to_head()
llist.print_list()