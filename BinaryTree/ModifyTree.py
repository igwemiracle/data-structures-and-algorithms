class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

# Modify a binary tree to get preorder traversal using right pointers only.


def ModifyTree(root):
    if not root:
        return None
    nodes = [root]
    prev = None
    while nodes:
        t = nodes.pop()
        if t.right:
            nodes.append(t.right)
        if t.left:
            nodes.append(t.left)
        if prev is not None:
            prev.right = t
        prev = t
# preorder traversal using only right pointers


def PreorderTraversal(root):
    while root:
        print(root.val, end=" ")
        root = root.right


if __name__ == "__main__":
    # Create the binary tree manually for demonstration purposes
    # You can modify this section to build the binary tree dynamically if needed.
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')

    ModifyTree(root)
    print("Preorder Traversal of right pointers only:")
    PreorderTraversal(root)
    print("")
