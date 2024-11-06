# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPossibleFBT(n):
    if n % 2 == 0:  # A full binary tree must have an odd number of nodes
        return []
    
    # Base case for one node
    if n == 1:
        return [TreeNode(0)]
    
    result = []
    for left_nodes in range(1, n, 2):  # left nodes can be 1, 3, ..., n-2
        right_nodes = n - 1 - left_nodes # Remaining nodes for the right subtree
        left_trees = allPossibleFBT(left_nodes)
        right_trees = allPossibleFBT(right_nodes)
        
        for left in left_trees:
            for right in right_trees:
                root = TreeNode(0)
                root.left = left
                root.right = right
                result.append(root)
    
    return result