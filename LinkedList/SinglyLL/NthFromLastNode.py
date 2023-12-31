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

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

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

            

llist = LinkedList()
llist.append("A")   
llist.append("B")     #
llist.append("C")
llist.append("D")

print(llist.print_nth_from_last(3))
# print(llist.print_nth_from_last(4,2))