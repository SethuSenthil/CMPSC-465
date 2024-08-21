class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(node, left=float('-inf'), right=float('inf')):
    if not node:
        return True
    if not (left < node.val < right):
        return False
    return (is_valid_bst(node.left, left, node.val) and
            is_valid_bst(node.right, node.val, right))

# Define the trees
# Tree 1
tree1 = TreeNode(10, TreeNode(9, TreeNode(8, TreeNode(6))))

# Tree 2
tree2 = TreeNode(8, TreeNode(4, TreeNode(3), TreeNode(6)),
                 TreeNode(10, TreeNode(9), TreeNode(13)))

# Tree 3
tree3 = TreeNode(4, TreeNode(3), TreeNode(9, TreeNode(8), TreeNode(10)))

# Tree 4
tree4 = TreeNode(4, TreeNode(3), TreeNode(9, TreeNode(10), TreeNode(8)))

# Check each tree
trees = [tree1, tree2, tree3, tree4]
results = [is_valid_bst(tree) for tree in trees]

# Print results
for i, result in enumerate(results, 1):
    print(f"Tree {i} is {'a valid BST' if result else 'not a valid BST'}")
