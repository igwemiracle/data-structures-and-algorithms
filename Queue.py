from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
#Using Queue data structure to keep track of inserted nodes
#from creating a Complete Binary Tree
class CompleteBinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.queue = deque()
    def insert(self, key):
        new_node = TreeNode(key)
        if not self.root:
            self.root = new_node
            self.queue.append(self.root)
        else:
            front = self.queue[0]
            if not front.left:
                front.left = new_node
            else:
                front.right = new_node
                self.queue.popleft()
            self.queue.append(new_node)


    def level_order_traversal(self):
        if not self.root:
            print("Tree is empty.")
            return

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            result.append(node.key)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("Level Order Traversal:", result)

tree = CompleteBinaryTree()
elements = [1, 2, 3, 4, 5, 6, 7]
for elem in elements:
    tree.insert(elem)

tree.level_order_traversal()


class Queue:
    def __init__(self) -> None:
        self.queue = []
    def addTop(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    def removeQ(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    def reverse(self):
        return self.queue.reverse()
    
    def print_queue(self):
        for i in self.queue:
            print(i)


    def size(self):
        return len(self.queue)



TheQueue = Queue()
TheQueue.addTop("Mon")
TheQueue.addTop("Tue")
TheQueue.addTop("Wed")
TheQueue.reverse()
TheQueue.print_queue()
# print(TheQueue.removeQ())
# print(TheQueue.removeQ())
print("The size of the queue is",TheQueue.size())


