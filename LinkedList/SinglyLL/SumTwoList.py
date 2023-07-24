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
            print(cur_node.data)
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


    def sum_two_lists(self, llist):
      p = self.head
      q = llist.head
      #List to store the sum of the two lists "p" and "q"
      sum_list = LinkedList() 
      carry = 0
      while p or q:
         if not p:
            i = 0
         else:
            i = p.data
         if not q:
            j = 0
         else:
            j = q.data
         s = i + j + carry
         if s >= 10:
            carry = 1
            remainder = s % 10
            sum_list.append(remainder)
         else:
            carry = 0
            sum_list.append(s)
         if p:
            p = p.next
         if q:
            q = q.next
      sum_list.print_list()

sumlist1 = LinkedList()
sumlist1.append(5) # Unit
sumlist1.append(6) # Tens
sumlist1.append(3) # Hundreds
sumlist2 = LinkedList()
sumlist2.append(8) # Unit
sumlist2.append(4) # Tens
sumlist2.append(2) # Hundreds
print("To check for the sum: ",365 + 248)
sumlist1.sum_two_lists(sumlist2)