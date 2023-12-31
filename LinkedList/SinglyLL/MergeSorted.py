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


    def merge_sorted(self, llist):
      p = self.head
      q = llist.head
      s = None

      if not p:
        return q

      if not q:
        return p
	
      if p and q:
        if p.data <= q.data:
          s = p
          p = s.next

        elif p.data <= q.data:
          s = q
          q = s.next
        # else:
        #   s = q
        #   q = s.next

        new_head = s

      while p and q:
        if p.data <= q.data:
          s.next = p
          s = p
          p = s.next

        else:
          s.next = q
          s = q
          q = s.next

      if not p:  # This means, since p is None("End of list") 
        s.next = q # let the next node(s.next) equals q
        
      if not q: # This means, since q is None("End of list") 
        s.next = p # let the next node(s.next) equals p

      self.head = new_head
      return self.head

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()