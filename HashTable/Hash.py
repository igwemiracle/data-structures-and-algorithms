class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

# Define a function to perform an inorder traversal of a binary tree


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)


# using a hash table to keep track of the nodes and their indices
# for a Binary tree.
def create_tree(parent):
    n = len(parent)
# Initialize an empty dictionary to keep track of nodes created so far
    nodes = {}
    root = None
    for i in range(0, n):
        # If the current node is the root node, create it
        if parent[i] == -1:
            root = Node(i)
            nodes[i] = root
        else:
            # If the parent node exists, get it from the dictionary
            parent_node = nodes.get(parent[i], None)
            # If the parent node does not exist yet, create it
            if parent_node is None:
                parent_node = Node(parent[i])
                nodes[parent[i]] = parent_node
# Create a new node and link it to its parent node
            current_node = Node(i)
            if parent_node.left is None:
                parent_node.left = current_node
            else:
                parent_node.right = current_node
            # Add the new node to the dictionary
            nodes[i] = current_node
    # Return the root node of the constructed tree
    return root


parent = [-1, 0, 0, 1, 1, 3, 5]
root = create_tree(parent)

print("Inorder traversal of constructed tree:")
inorder(root)
# Time complexity:  O(n), since we need to visit each node of the tree exactly once.
# Space complexity: O(h), where h is the height of the tree
print("")
