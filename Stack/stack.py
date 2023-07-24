class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('H')
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

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print("The head is:",stack.head.data)
    print(f"stack: {stack}")
    print("-------------------------------------")
    print("The size of the elements in stack is:",stack.getSize())
    print("-------------------------------------")
    print("The element at the top of the stack is:",stack.peek())
    print("-------------------------------------")
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")

    