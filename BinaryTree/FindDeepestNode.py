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
print("")