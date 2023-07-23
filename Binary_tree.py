class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s
        
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from collections import deque
#Finds the deepest and rightmost node in binary tree and replace 
#with the node we want to delete
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_deepest_rightmost_node(root):
    if not root:
        return None

    queue = deque([root])
    deepest_rightmost_node = None

    while queue:
        level_size = len(queue)
        deepest_rightmost_node = queue[-1]  # Rightmost node in the current level

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return deepest_rightmost_node

def delete_deepest_rightmost_node(root, deepest_rightmost_node):
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.left:
            if node.left == deepest_rightmost_node:
                node.left = None
                return
            else:
                queue.append(node.left)
        if node.right:
            if node.right == deepest_rightmost_node:
                node.right = None
                return
            else:
                queue.append(node.right)

def delete_node_from_tree(root, key):
    if not root:
        return None

    # Find the node to be deleted and the deepest rightmost node
    deepest_rightmost_node = find_deepest_rightmost_node(root)
    node_to_delete = None

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.data == key:
            node_to_delete = node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    if not node_to_delete:
        print("Node with the given key not found.")
        return root

    # Replace the node to be deleted with the data of the deepest rightmost node
    node_to_delete.data = deepest_rightmost_node.data

    # Delete the deepest rightmost node
    delete_deepest_rightmost_node(root, deepest_rightmost_node)

    return root

# Helper function to print the binary tree in level order
def print_level_order(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#Check for duplicates using tree serialization and hashing
#Using post-order traversal
def serialize_subtree(root, Hash_table):
    if not root:
        return "*"
    L_serialized = serialize_subtree(root.left, Hash_table)
    R_serialized = serialize_subtree(root.right, Hash_table)
    #Post_order = Left -> Right -> Root
    Serialized = L_serialized + "," + R_serialized + "," + str(root.data)

    if Serialized in Hash_table:
        Hash_table[Serialized] += 1
    else:
        Hash_table[Serialized] = 1
    return Serialized

def contains_duplicate_subtree(root):
    subtree_map = {}
    serialize_subtree(root, subtree_map)
    
    for sub_key, sub_value in subtree_map.items():
        if sub_value >= 2 and sub_key != "*":
            return True
    return False


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('B')
root.right.right.right = TreeNode('E')
root.right.right.left= TreeNode('D')
print(contains_duplicate_subtree(root))
# TIME COMPLEXITY: O(n)
# AUXILIARY SPACE: O(n)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(5)
# print(contains_duplicate_subtree(root))
print("")

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)

print("Before deletion:")
print_level_order(root)
print()

key_to_delete = 2
root = delete_node_from_tree(root, key_to_delete)

print("\nAfter deleting node with key", key_to_delete, ":")
print_level_order(root)
print("\n")


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
            # Recursive traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

            # Iterative traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
		#❌ To check if start is None, else:
        #❌ and recursively call inorder_print on start.left
		#❌ we append start.value to the traversal string
		#❌ and recursively call inorder_print on start.right
		#❌ traversal is just a string that will concatenate the value 
		#  of nodes in an order that we visited them.
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal


    def reverse_levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "_"
        
        return traversal

    def height(self, node):
      if node is None:
        return -1
      left_height = self.height(node.left)
      right_height = self.height(node.right)

      return 1 + max(left_height, right_height)
# Calculate height of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# Iterative approach
    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

# Recursive approach
    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)
# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5

# SIZE: the size of a binary tree is the total number of nodes. 


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
# print(tree.size())
print("The size of Tree is ",tree.size_(tree.root))
print("")



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(str("the height of the binary tree is ") + str(tree.height(tree.root)))
print("\n")


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree("reverse_levelorder"))
print("\n")


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.print_tree("levelorder"))
print("\n")


#1-2-4-5-3-6-7-
#4-2-5-1-6-3-7
#4-5-2-6-7-3-1
#                    1
#                 /      \
#               2          3  
#             /   \      /    \
#            4     5    6       7

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
        


