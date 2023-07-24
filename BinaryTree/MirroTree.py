class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Given two Trees return True if there are Mirror
# of each other


def MirrorTree(Tree1, Tree2):
    # Base case
    if Tree1 is None and Tree2 is None:
        return True

    if Tree1 is None or Tree2 is None:
        return False

    return (Tree1.data == Tree2.data and
            MirrorTree(Tree1.left, Tree2.right) and
            MirrorTree(Tree1.right, Tree2.left)
            )


root1 = TreeNode(1)
root2 = TreeNode(1)

root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.right.left = TreeNode(5)
root2.right.right = TreeNode(4)

if MirrorTree(root1, root2):
    print("Yes")
else:
    print("No")
