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
			print(cur.data)
			cur = cur.next


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


	def delete(self, key):
		cur = self.head
		while cur:
			if cur.data == key and cur == self.head:
				# case 1
				if not cur.next:
					cur = None
					self.head = None
					return

				# case 2
				else:
					nxt = cur.next
					cur.next = None
					nxt.prev = None
					cur = None
					self.head = nxt
					return

			elif cur.data == key:
				# case 3
				if cur.next:
					nxt = cur.next
					prev = cur.prev
					prev.next = nxt
					nxt.prev = prev
					cur.next = None
					cur.prev = None
					cur = None
					return

				# case 4
				else:
					prev = cur.prev
					prev.next = None
					cur.prev = None
					cur = None
					return
		cur = cur.next


	def delete_node(self, node):
		cur = self.head
		while cur:
			if cur == node and cur == self.head:
				# case 1
				if not cur.next:
					cur = None
					self.head = None
					return

				# case 2
				else:
					nxt = cur.next
					cur.next = None
					nxt.prev = None
					cur = None
					self.head = nxt
					return

			elif cur == node:
				# case 3
				if cur.next:
					nxt = cur.next
					prev = cur.prev
					prev.next = nxt
					nxt.prev = prev
					cur.next = None
					cur.prev = None
					cur = None
					return

				# case 4
				else:
					prev = cur.prev
					prev.next = None
					cur.prev = None
					cur = None
					return
		cur = cur.next


	def reverse(self):
		tmp = None
		cur = self.head
		while cur:
			tmp = cur.prev
			cur.prev = cur.next
			cur.next = tmp
			cur = cur.prev
		if tmp:
			self.head = tmp.prev
		 
	def remove_duplicates(self):
		cur = self.head
		seen = dict()
		while cur:
			if cur.data not in seen:
				seen[cur.data] = 1
				cur = cur.next
			else:
				nxt = cur.next
				self.delete_node(cur)
				cur = nxt

	def pairs_with_sum (self, sum_vals):
		pairs = list()
		p = self.head
		q = None
		while p:
			q = p.next
			while q:
				if p.data + q.data == sum_vals:
					pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
				q = q.next
			p = p.next
		return pairs


# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.prepend(4)


# dllist.print_list()


# dllist = DoublyLinkedList()
# dllist.append(8)
# dllist.append(4)
# dllist.append(4)
# dllist.append(6)
# dllist.append(4)
# dllist.append(8)
# dllist.append(4)
# dllist.append(10)
# dllist.append(12)
# dllist.append(12)
# dllist.remove_duplicates()
# dllist.print_list()



dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()

# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)

# dllist.delete(1)
# dllist.delete(6)
# dllist.delete(2)
# dllist.print_list()


# dllist = DoublyLinkedList()
# dllist.append("A")
# dllist.append("B")
# dllist.append("C")
# dllist.append("D")
# dllist.add_before_node("A", "G")
# dllist.print_list()

# print("\n")

# dllist = DoublyLinkedList()
# dllist.append("A")
# dllist.append("B")
# dllist.append("C")
# dllist.add_after_node("A", "E")
# dllist.print_list()



# dllist = DoublyLinkedList()
# dllist.prepend(0)
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.prepend(5)

# dllist.print_list()