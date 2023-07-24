class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

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
      

llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)

print(f"The occurrence of Node 1 is {llist_2.count_occurences_iterative(1)}")
print("Recursive methode: ")
print(llist_2.count_occurences_recursive(llist_2.head, 1))