from data_structures.bst import *

# ===== Problem Statement ===== #
# Given the root node of a binary search tree, return the sum
# of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.



class Solution:

    # Runtime: 304 ms
    # Memory: 22.1 MB
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        if root:
            # Only add to total value if root.val
            # meets the requested constraints
            if root.val >= L and root.val <= R:
                total += root.val

            # The total value on the current level of
            # recursion will be added with the total
            # values deeper in the recursion
            total += self.rangeSumBST(root.left, L, R)
            total += self.rangeSumBST(root.right, L, R)
        return total



if __name__ == "__main__":
    #             10
    #          /      \
    #        5         15
    #       / \      /   \
    #     3    7   null  18
    # Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    # Target Output: 32
    bst = BST()
    tree_vals = [10,5,15,3,7,18]
    for val in tree_vals:
        bst.insert(TreeNode(val))

    sol = Solution()
    L, R = 7, 15
    result = sol.rangeSumBST(bst.root, L, R)
    print(result)
