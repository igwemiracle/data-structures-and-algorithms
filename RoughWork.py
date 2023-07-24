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
            print(cur.data)
            cur = cur.next

    def add_at_front(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            new_node = Node(data)
            curr = self.head
            new_node.next = self.head
            new_node.prev = None
            curr.prev = new_node
            self.head = new_node

    def add_in_btwn(self,prev_node,data):
        if prev_node is None:
            print("This node does not exist")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

class Stack:
    def __init__(self):
        self.head = Node('Head')
        self.size = 0
    def __str__(self) -> str:
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]
    
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.data
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("poping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        return remove.data

class Conversion:

	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		
		# This array is used a stack
		self.array = []
		
		# Precedence setting
		self.output = []
		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

	# Check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False

	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]

	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# A utility function to check is the given character
	# is operand
	def isOperand(self, ch):
		return ch.isalpha()

	# Check if the precedence of operator is strictly
	# less than top of stack or not
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	# The main function that
	# converts given infix expression
	# to postfix expression
	def infixToPostfix(self, exp):

		# Iterate over the expression for conversion
		for i in exp:
			
			# If the character is an operand,
			# add it to output
			if self.isOperand(i):
				self.output.append(i)

			# If the character is an '(', push it to stack
			elif i == '(':
				self.push(i)

			# If the scanned character is an ')', pop and
			# output from the stack until and '(' is found
			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			# An operator is encountered
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		# Pop all the operator from the stack
		while not self.isEmpty():
			self.output.append(self.pop())

		for ch in self.output:
			print(ch, end=" ")


# Find the Maximum Achievable Number
class Solution:
    def alternatingSubarray(self, A: list[int]) -> int:
        n = len(A) #length is 6
        res = -1
        dp = -1
        for i in range(1, n):
            if dp > 0 and A[i] == A[i - 2]:
                dp += 1
            else:
                if A[i] == A[i - 1] + 1:
                    dp = 2
                else:
                    -1
            res = max(res, dp)
        return res

result = Solution()
a = result.alternatingSubarray([ -5, -1, -1, 2, -2, -3 ])
print(a)


# ❌# Driver code
# if __name__ == '__main__':
# 	exp = "(A+B)*(C+D)"
# 	obj = Conversion(len(exp))

# 	# Function call
# 	obj.infixToPostfix(exp)
          

# ❌if __name__ == "__main__":
#     stack = Stack()
#     for i in range(1, 11):
#         stack.push(i)
#     print("The head is:",stack.head.data)
#     print(f"stack: {stack}")


    # for _ in range(1, 6):
    #     remove = stack.pop()
    #     print(f"Pop: {remove}")
    # print(f"Stack: {stack}")




# ❌double = DoublyLinkedList()
# node = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# double.head = node
# double.head.next = node2
# node2.next = node3
# double.add_at_front("At_Front")
# # double.add_in_btwn(node2,"In btwn")
# double.InsertBefore(node2, "G")

# double.add_at_front("A")
# double.add_at_front("B")
# double.add_at_front("C")
# double.add_at_front(5)
# double.add_in_btwn("A",66)
# double.print_list()
