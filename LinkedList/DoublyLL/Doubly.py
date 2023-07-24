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

	def print_list(self):
		cur = self.head
		while cur:
			print(cur.data, end=" ")
			cur = cur.next

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		new_node.prev = None

		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def find_size(self):
		count = 0
		cur = self.head
		while cur:
			cur = cur.next
			count += 1
		return count
	
	def max_node(self):
		cur = self.head
		maxx = self.head    
		while cur:
			if cur.data > maxx.data:
				maxx = cur
			cur = cur.next
		return maxx.data

dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
print("")
double = DoublyLinkedList()
double.append(1)
double.append(23)
double.append(39)
double.append(40)
print("The nodes are: ")
double.print_list()
print("")
print("The size of the list is ",double.find_size())
print("maximum node is ",double.max_node())
print("")