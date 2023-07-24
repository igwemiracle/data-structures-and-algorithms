class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Check for duplicates using tree serialization and hashing
# Using post-order traversal


def serialize_subtree(root, Hash_table):
    if not root:
        return "*"

    L_serialized = serialize_subtree(root.left, Hash_table)
    R_serialized = serialize_subtree(root.right, Hash_table)
    # Post_order = Left -> Right -> Root
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
root.right.right.left = TreeNode('D')
print(contains_duplicate_subtree(root))
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(5)
# print(contains_duplicate_subtree(root))
# TIME COMPLEXITY: O(n)
# AUXILIARY SPACE: O(n)
