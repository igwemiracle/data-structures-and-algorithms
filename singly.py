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

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                print("cur_node = ", cur_node.data)
                cur_node = None
                return

            prev = None
            count = 1
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1


            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):

        prev = None 
        cur = self.head
        while cur:  # while cur is not None or is not the end of the list
            nxt = cur.next
            cur.next = prev
            
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            prev = cur 
            cur = nxt 
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
        
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
        
            
    def remove_duplicates(self):
      cur = self.head
      prev = None  
      dup_values = dict()

      while cur:
        if cur.data in dup_values:
          # Remove node
          prev.next = cur.next
          cur = None
        else:
          # Have not encountered before
          dup_values[cur.data] = 1
          prev = cur
        cur = prev.next


    def print_nth_from_last(self, n):
      # METHOD 1:
          # <------------>
            # total_len = self.len_iterative()
            # cur = self.head 
            # while cur:
            #     if total_len == n:
            #        print(cur.data)
            #        return cur.data
            #     total_len -= 1
            #     cur = cur.next
            # if cur is None:
            #     return
            

            # METHOD 2
           # <----------->

           p = self.head 
           q = self.head

           count = 0
           while q and count < n:
             q = q.next
             count += 1

           if not q:
             print( str(n) + "is greater than the number of nodes in list." )  
             return

           while p and q:
             p = p.next
             q = q.next
           return p.data         

 

      # ITERATIVE OCCOURENCES 
    def count_occurences_iterative(self, data):
      count = 0
      cur = self.head

      while cur:
        if cur.data == data:
          count += 1
        cur = cur.next  # If the current data ("cur.data") equals the data we are looking for
      return count

       
      # RECURSIVE OCCOURENCES

    def count_occurences_recursive(self, node, data):  
      # node will act as the current node that we are on
      # data will act as the number of occurences we checking
      if not node:
        return 0
    # base case written above in line 261 and 262 is an empty linked list

      if node.data == data:
        return 1 + self.count_occurences_recursive(node.next, data)
      else:
         return self.count_occurences_recursive(node.next, data)


    def rotate(self, k):
      p = self.head
      q = self.head

      prev = None
      count = 0
      while p and count < k:
        prev = p
        p = p.next
        q = q.next
        count += 1
      p = prev
      
      while q:
        prev = q
        q = q.next
      q = prev

      q.next = self.head
      self.head = p.next
      p.next = None


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


    def sum_two_lists(self, llist):
      p = self.head
      q = llist.head

      sum_list = LinkedList()
      # "sum_list" will represent the final sum at the end of this method

      carry = 0  # helps in evaluating the sum
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


    
# 3 6 5 
# 2 4 8 
# -----
#.6 1 3
# -----  
llist1 = LinkedList()
llist1.append(13) # Unit
llist1.append(21) # Tens
llist1.append(34) # Hundreds
llist1.append(42)
llist1.append(50)
llist1.delete_node_at_pos(0)
llist1.print_list()
# llist2 = LinkedList()
# llist2.append(8) # Unit
# llist2.append(4) # Tens
# llist2.append(2) # Hundreds

# print(365 + 248)
# llist1.sum_two_lists(llist2)






# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# # A -> B -> C -> D -> Null
# D -> A -> B -> C -> Null
# llist.print_list()
# llist.move_tail_to_head()
# print("\n")
# llist.print_list()



# llist = LinkedList()
# llist.append("R")
# llist.append("A")
# llist.append("D")
# llist.append("A")                
# llist.append("R")

# llist_2 = LinkedList()
# llist_2.append("A")
# llist_2.append("B")
# llist_2.append("C")

# print(llist.is_palindrome())
# print(llist_2.is_palindrome())



# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)

# llist.print_list()
# print("\n")
# llist.rotate(4)
# llist.print_list()



# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_iterative(1))
# print(llist_2.count_occurences_recursive(llist_2.head, 1))



# llist = LinkedList()
# llist.append("A")   
# llist.append("B")     #
# llist.append("C")
# llist.append("D")

# print(llist.print_nth_from_last(2))
# print(llist.print_nth_from_last(4,2))



# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()


# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.reverse_iterative()
# llist.reverse_recursive()
# llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()
