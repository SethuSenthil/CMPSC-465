class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree_from_array(arr):
    if not arr:
        return None

    nodes = [None if val == '-' else TreeNode(int(val)) for val in arr]

    for i in range(len(arr)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

    return nodes[0]

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.val < max_val):
        return False
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)

def check_if_valid_bst(arr_string):
    arr = arr_string.split()
    root = construct_tree_from_array(arr)
    return is_valid_bst(root)

# Example usage
input_string = "3 5 6 9 8 7 10"
print(check_if_valid_bst(input_string))  # Output: False (Based on the given analysis)