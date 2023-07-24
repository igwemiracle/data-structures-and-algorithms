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

    def is_palindrome(self):
    # <---------------------------->
      # METHOD 1: using string
    # <--------------------------->
      # s = ""
      # p = self.head
      # while p:
      #   s += p.data
      #   p = p.next
      # return s == s[::-1]
      
    # <---------------------------->
      # METHOD 2: using stack
    # <---------------------------->
      # s = []
      # p = self.head
      # while p:
      #   s.append(p.data)
      #   p = p.next
      # p = self.head
      # while p:
      #   data = s.pop()
      #   if data != p.data:
      #     return False
      #   p = p.next
      # return True

     # <---------------------------->
      # METHOD 3: using two pointers
    #  <---------------------------->
      p = self.head
      q = self.head
      prev = []

      i = 0
      while q:
        prev.append(q)
        q = q.next
        i += 1
      q = prev[i-1]
      
      count = 1
      while count <= 1//2 + 1:
        if prev[-count].data != p.data:
          return False
        p = p.next
        count += 1
      return True

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")                
llist.append("R")

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print("Is this a palindrome? ",llist.is_palindrome())
print("Is this a palindrome?",llist_2.is_palindrome())